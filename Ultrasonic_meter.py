from machine import Pin, I2C 
from ssd1306 import SSD1306_I2C 
import utime 

# define OLED dimensions
WIDTH = 128
HEIGHT = 64

# define OLED object and pins connected to pico
i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=200000)
display = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# define trig and echo pins of ultra sonic sensor connected to pico
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

# define a function to check the distance
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
    return timePassed # the return value is a time not the distance

# put the main program in a while loop
while True:
    distance = CheckDistance()
    # print(distance)
    distance_cm = (distance * 0.0343) / 2 # distance in Centi meters
    # print(distance_cm)
    display.fill(0) # to clear out the OLED display
    display.text("Distance: ", 0 , 0) # prints Distance on OLED
    display.text(str(round(distance_cm, 2)) + " CM", 0 , 16) # prints distance in centi meters on OLED
    if distance_cm > 100: # check if the distance reaches a meter and display the distance in meters
        distance_m = round((distance_cm/100),2)
        display.text(str(distance_m) + " M", 0, 33)
    utime.sleep(0.5) # refresh rate of the distance meter
    display.show()
