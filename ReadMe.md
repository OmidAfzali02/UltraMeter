This project is made with Raspberry pi pico and using python language.

Ultra sonic sensor uses sound waves to measure its distance from an object.

To create this ultrasonic meter you need to following hardware:
    1.Raspberry pi pico
    2.Ultra sonic sensor HC-SR04
    3.OLED I2C with SSD1306 driver 128*64 px

Follow the Diagram.png file instructions and make the necessary connections.
![Alt text](https://github.com/OmidAfzali02/UltraMeter/blob/main/Diagram.png)

Now you can use the code on Ultrasonic_meter.py file and then your project is final.
```
from machine import Pin, I2C
```