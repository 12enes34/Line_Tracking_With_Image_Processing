import time
import cv2
import numpy as np

import requests

esp_ip = "192.168.137.166"
esp_port = 80
url = f"http://{esp_ip}:{esp_port}/"

def send_command(command):
    try:
        response = requests.post(url, data=command)
        if response.status_code == 200:
            print(f"Command '{command}' sent successfully.")
        else:
            print(f"Failed to send command '{command}'. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error sending command1'{command}': {e}")

# Motorları kontrol etme fonksiyonları
def control_left_motor(rotation=1, speed=100):
    command = f"LEFT,{rotation},{speed}"
    send_command(command)

def control_right_motor(rotation=1, speed=100):
    command = f"RIGHT,{rotation},{speed}"
    send_command(command)

def back_and_forth(rotation=1, speed=100):
    command = f"BackAndForth,{rotation},{speed}"
    send_command(command)


def g_turn(rotation=1, speed=200):
    command = f"G_Turn,{rotation},{speed}"
    send_command(command)

def control_upper_motor(rotation=1, speed=200):
    command = f"Upper,{rotation},{speed}"
    send_command(command)

def control_right_left_motor(right_motor_pwm=100,left_motor_pwm=100,rotation=1):
    command = f"2BackAndForth,{right_motor_pwm},{left_motor_pwm},{rotation}"
    send_command(command)


"""ARDUINOYA KOD EKLENECEK Eklendi Test edilmesi gerek"""

def control_right_left_motor_with_rotations(right_motor_pwm=100,left_motor_pwm=100,RightRotation=1,LeftRotation=1):
    command = f"3BackAndForth,{right_motor_pwm},{left_motor_pwm},{RightRotation},{LeftRotation}"
    send_command(command)




# Mesafe ölçümü
def measure_distance():
    command = "MEASURE"
    send_command(command)

# Buzzer melodisini çaldırma
def play_buzzer():
    command = "BUZZER"
    send_command(command)







def Motor_Steer (port1,port2,speed,steering):
    if steering == 0:
        #BP.set_motor_speed(port1, speed)
        #BP.set_motor_speed(port2, speed)
        print('Aci yok Motor 1 hiz :', speed)
        print('Aci yok Motor 2 hiz :', speed)
        control_right_left_motor_with_rotations(speed,speed,1,1)
        
        #2 different way

        """
        #RightPwm , LeftPwm , RightRot , LeftRot
        control_right_left_motor_with_rotations(right_motor_pwm=100,left_motor_pwm=100,RightRotation=1,LeftRotation=1)
        control_right_left_motor_with_rotations()
        """
        return
    
    elif steering > 0:
        steering = 100 -steering
        #BP.set_motor_speed(port2, speed)
        #BP.set_motor_speed(port1, speed*steering/100)
        print('Aci pozitif Motor 1 hiz :', (speed*steering/100) )
        print('Aci pozitif Motor 2 hiz :', speed)

        if (speed*steering/100) > 0:
            rotR = 1
        else:
            rotR = 0

        if speed > 0:
            rotL = 1
        else:
            rotL = 0
    
        control_right_left_motor_with_rotations((speed*steering/100),speed,rotR,rotL)
        return
    
    elif steering < 0:
        steering = steering * -1
        steering = 100 - steering
        #BP.set_motor_speed(port1, speed)
        #BP.set_motor_speed(port2, speed*steering/100)
        print('Aci pozitif Motor 1 hiz :', speed )
        print('Aci pozitif Motor 2 hiz :', (speed*steering/100) )

        if speed > 0:
            rotR = 1
        else:
            rotR = 0

        if (speed*steering/100) > 0:
            rotL = 1
        else:
            rotL = 0
    
        control_right_left_motor_with_rotations((speed*steering/100),speed,rotR,rotL)

        return






























# Kamerayı aç
camera = cv2.VideoCapture(1)  # Varsayılan kamera cihazını (genellikle bilgisayarın dahili kamerası) açar

# Çözünürlüğü ayarla
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Kameranın genişliğini 640 piksel olarak ayarlar
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)  # Kameranın yüksekliğini 360 piksel olarak ayarlar

# Kamera açılamazsa çıkış yap
if not camera.isOpened():
    print("Kamera açılamadı")  # Kamera açılamazsa hata mesajı yazdırır
    exit()  # Programdan çıkış yapar

#Tespit edilen ilk konturun lokasyonu #bunun sayesinde ekranda belirlenen ve ekranin altina dogru giden cizgileri yok sayariz bu da dogru yolu izlememize olanak verir
x_last = 320
y_last = 180

start_tine = time.time()
counter = 0



    
kp = .75
ap = 1

TrasholdDownLimit   = (0, 0, 0)
TrasholdUpLimit     = (135,135,136)




while True:
    counter+=1
    # Kameradan kareyi oku
    ret, frame = camera.read()  # Kameradan bir kare okur

    # Okuma başarılı olmadıysa döngüden çık
    if not ret:
        print("Kare okunamadı")  # Kare okuma başarısız olursa hata mesajı yazdırır
        break  # Döngüden çıkar


    # Görüntü işleme ve kontur bulma
    """Alt ve ust sinirlari bulup islemi ona gore dizayn edecegiz"""
    Blackline = cv2.inRange(frame, TrasholdDownLimit, TrasholdUpLimit)  # Görüntüde siyah renk aralığındaki pikselleri bulurorjınal (75,75,75)


    # Kernel tanımla
    kernel = np.ones((3, 3), np.uint8)  # 3x3 boyutunda, tüm elemanları 1 olan bir kernel oluştur

    # Erozyon işlemi uygula
    Blackline = cv2.erode(Blackline, kernel, iterations=4)  # Siyah çizgiler üzerinde 5 iterasyonluk erozyon işlemi uygula
    
    # Dilate işlemi uygula #Cozunurluk dusuk ise iptal edilebilir
    Blackline = cv2.dilate(Blackline, kernel, iterations=9)  # Siyah çizgiler üzerinde 9 iterasyonluk dilate işlemi uygula

    # OpenCV sürümüne göre cv2.findContours fonksiyonunu çağır
    contours_blk, hierarchy_blk = cv2.findContours(Blackline.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Blackline görüntüsündeki konturları bulur
    # cv2.RETR_TREE: Tüm konturları ve hiyerarşilerini döndürür
    # cv2.CHAIN_APPROX_SIMPLE: Kontur noktalarının sadece köşe noktalarını tutar

    # Konturları çiz
    """Cizgi Etrafina Yesil renk ile sinirlarini cizer"""
    """cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)"""
    # Orijinal görüntü üzerinde bulunan konturları yeşil renk ile çizer
    # -1: Tüm konturları çizer
    # (0, 255, 0): Renk (yeşil)
    # 3: Çizgi kalınlığı

    


    contours_blk_len = len(contours_blk)
    if contours_blk_len > 0 :
        if contours_blk_len == 1 :
            blackbox = cv2.minAreaRect(contours_blk[0])
        else:
            canditates=[]
            off_bottom = 0
            for con_num in range(contours_blk_len):
                blackbox = cv2.minAreaRect(contours_blk[con_num])
                (x_min, y_min), (w_min, h_min) , ang = blackbox
                box = cv2.boxPoints(blackbox)
                (x_box,y_box) = box[0]
                if y_box > 358 : #Ekranin yuksekliginden 2 pixel az
                    off_bottom +=1
                
                canditates.append((y_box,con_num,x_min,y_min))
            canditates = sorted(canditates)
            if off_bottom > 1:
                canditates_off_bottom=[]
                for con_num in range ((contours_blk_len - off_bottom), contours_blk_len):
                    (y_highest,con_highest,x_min,y_min) = canditates[con_num]
                    total_distance = (abs(x_min - x_last)**2 + abs(y_min - y_last)**2)**0.5
                    canditates_off_bottom.append((total_distance,con_highest))
                canditates_off_bottom = sorted(canditates_off_bottom)
                (total_distance,con_highest) = canditates_off_bottom[0]
                blackbox = cv2.minAreaRect(contours_blk[con_highest])
                
            else:
                (y_highest,con_highest,x_min,y_min) = canditates[contours_blk_len-1]
                blackbox = cv2.minAreaRect(contours_blk[con_highest])



        (x_min, y_min), (w_min, h_min), ang = blackbox
        x_last = x_min
        y_last = y_min
        if ang < -45 :
            ang = 90 + ang 
        if w_min < h_min and ang > 0:
            ang = (90-ang)*-1
        if w_min > h_min and ang < 0:
            ang = 90 + ang

        setpoint = 320
        error = int(x_min - setpoint)
        ang = int(ang)
        Motor_Steer("BP.PORT_A", "BP.PORT_D", 120, (error*kp)+(ang*ap))
        box = cv2.boxPoints(blackbox)
        box = np.int0(box)
        cv2.drawContours(frame,[box],0,(0,0,255),3)
        cv2.putText(frame,str(ang), (10,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        cv2.putText(frame,str(error), (10,320), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        cv2.line(frame, (int(x_min),200 ) , (int(x_min),250 ), (255,0,0),3)

        # Dikey bir kılavuz çizgisi çiz
        
        #cv2.line(frame, (x_blk + (w_blk // 2), 0), (x_blk + (w_blk // 2), 360), (255, 0, 0), 3)
        # (x + (w // 2), 0): Çizginin başlangıç noktası, dikdörtgenin ortasından, görüntü yüksekliğinin üstünden
        # (x + (w // 2), 360): Çizginin bitiş noktası, dikdörtgenin ortasından, görüntü yüksekliğinin altından
        # (255, 0, 0): Renk (mavi)
        # 3: Çizgi kalınlığı
        # Kareyi göster


    cv2.imshow('Original with line', frame)  # Görüntüyü ekranda gösterir
    # cv2.imshow("Green", Greensign)
    # 'q' tuşuna basılırsa döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # 'q' tuşuna basılırsa döngüden çıkar ve programı sonlandırır

    if cv2.waitKey(1) & 0xFF == ord('e'):
        TrasholdDownLimit2 = list(TrasholdDownLimit)

        TrasholdUpLimit2  = list(TrasholdUpLimit)
        choice = input('\nTrashold Down Limit : 1 \nTrashold Up Limit : 2 \nShow : 3 \n')
        if choice == '1':
            Red ,Green ,Blue = TrasholdDownLimit2
            color = input('R,G,B: ')
            if color == 'R':
                Red = int(input('Trashold Down Limit Red: '))
            elif color == 'G':
                Green = int(input('Trashold Down Limit Green: '))
            elif color == 'B':
                Blue = int(input('Trashold Down Limit Blue: '))
            TrasholdDownLimit = (Red,Green,Blue)

        if choice == '2':
            Red ,Green ,Blue = TrasholdUpLimit2
            color = input('R,G,B: ')
            if color == 'R':
                Red = int(input('Trashold Up Limit Red: '))
            elif color == 'G':
                Green = int(input('Trashold Up Limit Green: '))
            elif color == 'B':
                Blue = int(input('Trashold Up Limit Blue: '))
            TrasholdUpLimit = (Red,Green,Blue)
        
        if choice == '3':
            print(f'Trashold Down Limit : {TrasholdDownLimit} Trashold Down Limit2 : {TrasholdDownLimit2} Trashold Up Limit : {TrasholdUpLimit} Trashold Up Limit2 : {TrasholdUpLimit2} ')
            

# Her şeyi serbest bırak
finish_time = time.time()
fps = counter / (finish_time - start_tine)
print("frames per second = " + str(fps))
camera.release()  # Kamerayı serbest bırakır
cv2.destroyAllWindows()  # Tüm OpenCV pencerelerini kapatır