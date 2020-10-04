from gpiozero import DistanceSensor
from gpiozero import Robot
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import math


#Remote GPIO pin setting
#For Rpi 4B
factory1 = PiGPIOFactory(host='192.168.1.3')

#For RPi Zero
factory2 = PiGPIOFactory(host='192.168.1.3')

#connected to raspberry pi 4B
sensor1 = DistanceSensor(echo=18, trigger=26, factory=factory1)
sensor2 = DistanceSensor(echo=16, trigger=20, factory=factory1)

while True:
    print('Distance 1 : ', sensor1.distance * 100)
    print('Distance 2 : ', sensor2.distance * 100)
    sleep(5)
    r1 = sensor1.distance * 100
    r2 = sensor2.distance * 100

    x1 = r1 * math.cos(math.radians(90 - 90))
    z1 = r1 * math.sin(math.radians(90 - 90))
    y1 = 0.0

    x2 = r2 * math.cos(math.radians(90 - 40))
    z2 = r2 * math.sin(math.radians(90 - 40))
    y2 = 5.0

    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    print('Relative distance between Drone and obstacle : ', dist)

#Connected to Raspberry pi zero
robot1 = Robot(left=(21, 22, 26, factory=factory2), right=(4, 5, 6, factory=factory2))
robot2 = Robot(left=(23, 24, 25, factory=factory2), right=(27, 28, 29, factory=factory2 ))

for i in range(1):
    if dist > 1:
        robot1.forward()
        robot2.forward()
    else:
        robot1.stop()
        robot2.stop()
        sleep()
