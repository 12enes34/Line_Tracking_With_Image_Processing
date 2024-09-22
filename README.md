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
![Kamera Örnek Görüntü](görsel_linki)

- Siyah çizgi ortasında ki mavi çizgi eğimi ifade ediyor
- Sol üstteki kırmızı renkli sayı eğimi veriyor
- Sol ortadaki mavi renkli sayı hata oranını veriyor






















