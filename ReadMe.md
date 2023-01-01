This project is made with Raspberry pi pico and using python language.

Ultra sonic sensor uses sound waves to measure its distance from an object.

To create this ultrasonic meter you need to following hardware:
    1.Raspberry pi pico
    2.Ultra sonic sensor HC-SR04
    3.OLED I2C with SSD1306 driver 128*64 px

Follow the Diagram.png file instructions and make the necessary connections.
![Alt text](https://github.com/OmidAfzali02/UltraMeter/blob/main/Diagram.png)

Now you can use the code on Ultrasonic_meter.py file and then your project is final.
1. import libraries
```
from machine import Pin, I2C    # to connect your OS to pico
from ssd1306 import SSD1306_I2C # to connect to OLED
import utime    # to manipulate time
```

2. define OLED object and pins connected to pico
```
# define OLED dimensions
WIDTH = 128
HEIGHT = 64

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=200000) 
display = SSD1306_I2C(WIDTH, HEIGHT, i2c)
```

3. define trig and echo pins of ultra sonic sensor connected to pico
```
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
```

4. define a function to check the distance
```
def CheckDistance():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(1)
    trigger.low()
 
    while echo.value() == 0:
        delayTime = utime.ticks_us()
    while echo.value() == 1:
        receiveTime = utime.ticks_us()
    timePassed = receiveTime - delayTime
    # print(timePassed)
    return timePassed   # the return value is a time not the distance
```

5. put the main program in a while loop
```
while True:
    distance = CheckDistance()
    # print(distance)
    distance_cm = (distance * 0.0343) / 2   # distance in Centi meters
    # print(distance_cm)
    display.fill(0) # to clear out the OLED display
    display.text("Distance: ", 0 , 0)   # prints Distance on OLED
    display.text(str(round(distance_cm, 2)) + " CM", 0 , 16)    # prints distance in centi meters on OLED
    if distance_cm > 100:   # check if the distance reaches a meter and display the distance in meters
        distance_m = round((distance_cm/100),2)
        display.text(str(distance_m) + " M", 0, 33)
    utime.sleep(0.5)    # refresh rate of the distance meter
    display.show()
```

6. don't forget to always save Ultrasonic_meter.py file on your Raspberry pi pico device.


    .📫 How to reach me : dev.omid02@gmail.com
    . https://github.com/OmidAfzali02