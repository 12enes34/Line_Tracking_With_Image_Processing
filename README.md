# README in Two Languages: ESP Motor Control and Image Processing Project

- [Türkçe Bölüm](#turkce-bolum)
- [English Section](#english-section)


<h1 align="center" style="font-size: 62px;" id="turkce-bolum">TÜRKÇE</h1>
# ESP Motor Kontrol ve Görüntü İşleme Projesi

Bu proje, ESP modülü üzerinden motor kontrolü yaparak ve OpenCV kullanarak kamera görüntülerinde siyah çizgileri algılayarak PID algoritması ile çizgi takibi görevini yerine getirir. 

## Gereksinimler

- Python 3.x
- OpenCV (`cv2`) kütüphanesi
- NumPy kütüphanesi
- Requests kütüphanesi
- ESP8266/ESP32 modülü

## Kurulum

1. Gerekli Python kütüphanelerini yükleyin:

    ```bash
    pip install numpy opencv-python requests
    ```

2. ESP modülünüzü doğru şekilde yapılandırın ve IP adresini ayarlayın.

## Kullanım

### Motor Kontrol Fonksiyonları

Motorları ESP üzerinden kontrol etmek için aşağıdaki fonksiyonları kullanabilirsiniz:

- **Sol motoru kontrol etme:**

    ```python
    control_left_motor(rotation=1, speed=100)
    ```

- **Sağ motoru kontrol etme:**

    ```python
    control_right_motor(rotation=1, speed=100)
    ```

- **Motorları ileri ve geri hareket ettirme:**

    ```python
    back_and_forth(rotation=1, speed=100)
    ```

- **G dönüşü yapma:**

    ```python
    g_turn(rotation=1, speed=200)
    ```

- **Üst motoru kontrol etme:**

    ```python
    control_upper_motor(rotation=1, speed=200)
    ```

- **Sağ ve sol motorları aynı anda kontrol etme:**

    ```python
    control_right_left_motor(right_motor_pwm=100, left_motor_pwm=100, rotation=1)
    ```

- **Motorları belirli yönlerde döndürme:**

    ```python
    control_right_left_motor_with_rotations(right_motor_pwm=100, left_motor_pwm=100, RightRotation=1, LeftRotation=1)
    ```

### Mesafe Ölçümü

ESP modülüne mesafe ölçüm komutu göndermek için:

```python
measure_distance()
```

## Görüntü işleme kurulum

1. Gerekli Python kütüphanelerini yükleyin:

    ```Requirements
    pip install -r requirements.txt
    ```
    
## Kullanım

### Görüntü işleme kamera kontrol

Kameranızı değiştirmek için aşşağıda ki kod bloğundan kameranızı seçebilirsiniz:
0 Dahili kamera
1 harici kamera

- **Kamera değiştirmek için:**

    ```python
    camera = cv2.VideoCapture(0)
    ```
- **Kamera treshold değerlerini değiştrimek için e tuşuna basın:
-Trashold Down Limit İçin : 1 Trashold Up Limit İçin : 2 Show İçin : 3
Red İçin R , Green İçin G , Blue İçin B ye basın ve size en doğru treshold seçeneklerini belirleyin**

    ```python
    if cv2.waitKey(1) & 0xFF == ord('e'):
    ```

### PID hassasiyet kontrol

PID algoritması parametreleri:

  kp (Proportional Gain): Hata ile orantılı olan bu değer,
  sistemin ne kadar agresif şekilde hatayı düzeltmeye çalışacağını belirler.
  Hata arttıkça motor hızını artırarak daha hızlı düzeltme yapar.
  Bu parametre, motorların ne kadar hızlı tepki vereceğini ayarlar.
  Kodda kp = 0.75 olarak ayarlanmış, yani hata miktarının %75'i ile orantılı bir düzeltme uygulanıyor.

  ap (Angular Proportional Gain): Açısal hata düzeltme için kullanılan bu parametre,
  özellikle yönlendirme ile ilgili hataları düzeltmek için ayarlanır.
  ap = 1 olarak ayarlanmış, yani açısal hata miktarına doğrudan bir karşılık uygulanıyor.
  Bu değer, motorların yön değişimlerini ne kadar hızlı yapacağını kontrol eder.
  
- **kp ve ap degerlerini cihazınıza göre değiştirebilirsiniz:**

    ```python
    kp = .75
    ap = 1
    ```


# Örnek kamera görüntüsü
![Kamera Örnek Görüntü](https://github.com/12enes34/Line_Tracking_With_Image_Processing/blob/main/Screenshot%202024-09-22%20103050.png)
![Kamera Örnek Görüntü2](https://github.com/12enes34/Line_Tracking_With_Image_Processing/blob/main/Screenshot%202024-09-22%20103121.png)

- Siyah çizgi ortasında ki mavi çizgi eğimi ifade ediyor
- Sol üstteki kırmızı renkli sayı eğimi veriyor
- Sol ortadaki mavi renkli sayı hata oranını veriyor

# Prototip 

![Kamera Örnek Görüntü2](https://github.com/12enes34/Line_Tracking_With_Image_Processing/blob/main/%C3%87izgi_Takibi.gif)



<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>





<h1 align="center" style="font-size: 62px;" id="english-section">ENGLISH</h1>



































# ESP Motor Control and Image Processing Project

This project performs line tracking task with PID algorithm by controlling motor via ESP module and detecting black lines in camera images using OpenCV.

## Requirements

- Python 3.x
- OpenCV (`cv2`) library
- NumPy library
- Requests library
- ESP8266/ESP32 module

## Installation

1. Install required Python libraries:

```bash
pip install numpy opencv-python requests
```

2. Configure your ESP module correctly and set its IP address.

## Usage

### Motor Control Functions

You can use the following functions to control motors via ESP:

- **Control the left motor:**

```python
control_left_motor(rotation=1, speed=100)
```

- **Control the right motor:**

```python
control_right_motor(rotation=1, speed=100)
```

- **Move motors forward and backward:**

```python
back_and_forth(rotation=1, speed=100)
```

- **Make G turn:**

```python
g_turn(rotation=1, speed=200)
```

- **Control the upper motor:**

```python
control_upper_motor(rotation=1, speed=200)
```

- **Controlling right and left motors at the same time:**

```python
control_right_left_motor(right_motor_pwm=100, left_motor_pwm=100, rotation=1)
```

- **Rotating motors in specific directions:**

```python
control_right_left_motor_with_rotations(right_motor_pwm=100, left_motor_pwm=100, RightRotation=1, LeftRotation=1)
```

### Distance Measurement

To send distance measurement command to ESP module:

```python
measure_distance()
```

## Image processing installation

1. Install required Python libraries:

```Requirements
pip install -r requirements.txt
```

## Usage

### Image processing camera control

To change your camera, you can select your camera from the code block below:
0 Internal camera
1 External camera

- **To change camera:**

```python
camera = cv2.VideoCapture(0)
```
- **Press e to change camera threshold values:
-For Trashold Down Limit: 1 For Trashold Up Limit: 2 For Show: 3
Press R for Red, G for Green, B for Blue and select the most appropriate threshold options for you**

```python
if cv2.waitKey(1) & 0xFF == ord('e'):
```

### PID sensitivity control

PID algorithm parameters:

kp (Proportional Gain): This value, which is proportional to the error,
determines how aggressively the system will try to correct the error.
As the error increases, it increases the motor speed and corrects faster.
This parameter sets how fast the motors respond.

In the code, it is set to kp = 0.75, meaning that a correction proportional to 75% of the error amount is applied.

ap (Angular Proportional Gain): This parameter is used for angular error correction,
specifically set to correct errors related to orientation.
It is set to ap = 1, meaning that a direct response is applied to the amount of angular error.
This value controls how fast the motors change direction.

- **You can change the kp and ap values ​​according to your device:**

```python
kp = .75
ap = 1
```

# Sample camera image
![Camera Sample Image](https://github.com/12enes34/Line_Tracking_With_Image_Processing/blob/main/Screenshot%202024-09-22%20103050.png)
![Camera Sample Image2](https://github.com/12enes34/Line_Tracking_With_Image_Processing/blob/main/Screenshot%202024-09-22%20103121.png)

- The blue line in the middle of the black line indicates the slope
- The red number in the upper left gives the slope
- The blue number in the middle left gives the error rate

# Prototype 
![Camera Sample Image2](https://github.com/12enes34/Line_Tracking_With_Image_Processing/blob/main/%C3%87izgi_Takibi.gif)



