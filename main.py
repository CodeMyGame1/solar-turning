#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

class Parts():
    def __init__(self):
        self.ev3 = EV3Brick()
        #self.motorleft = Motor(Port.D)
        self.motorright = Motor(Port.A)
        self.right = ColorSensor(Port.S3)
        self.left = ColorSensor(Port.S2)
        #self.gyro = GyroSensor(Port.S4)
        self.leftambient = 0
        self.rightambient = 0
        self.delta = 0
        #self.savefile = open("testcheck.txt", "a")
    def check(self):
        self.leftambient = self.left.ambient()
        self.rightambient = self.right.ambient()
        self.delta = self.leftambient - self.rightambient
        return self.delta
        #print("LEFT: %d | RIGHT: %d" % (self.leftambient, self.rightambient))        
    def checkGyro(self):
        print(self.gyro)
brickthing = Parts()

def mainloop():
    #for x in range (20):
    while True:
        #checkedo = brickthing.check()
        #print(checkedo)
        '''if (checkedo == "TURN LEFT"):
            brickthing.motorleft.run_time(3, 1, Stop.HOLD, wait=True)
        elif (checkedo == "TURN RIGHT"):
            brickthing.motorleft.run_time(3, 1, Stop.HOLD, wait=True)
        elif (checkedo == "STAY"):
            print("STAY")'''
        '''if (checkedo > 4):
            brickthing.motorleft.run_target(500, 90)
        elif (checkedo < -4):
            brickthing.motorright.run_target(500, 90)'''
        while True:#brickthing.check() > 1 or brickthing.check() < -1:
            print("LEFT: " + str(brickthing.leftambient))
            print("RIGHT: " + str(brickthing.rightambient))
            print("DELTA: " + str(brickthing.check()))
            print("ANGLE MOTORRIGHT: " + str(brickthing.motorright.angle())) #91 and -4 
            print(str(brickthing.check()) + "--1")
            brickthing.motorright.run_angle(10, 10) #done
            time.sleep(2) #done
            '''if (brickthing.check() > 1):
                if (brickthing.motorright.angle() < -70):
                    print("OVERRIDE")
                    continue
                else:
                #brickthing.motorleft.run_angle(10, -10)
                    brickthing.motorright.run_angle(10, 10) #10 left
                    print("TURNED THIS WAY")
            elif (brickthing.check() < -1):
                if (brickthing.motorright.angle() > 70):
                    print("OVERRIDE")
                    continue
                else:
                    #brickthing.motorleft.run_angle(10, 10)
                    brickthing.motorright.run_angle(10, -10) #-10 right
                    print("TURNED THAT WAY")
            #brickthing.savefile.write("LEFT: %d | RIGHT: %d" % (brickthing.leftambient, brickthing.rightambient))'''
        print(brickthing.check())
        print("BREAK")
        time.sleep(5)
    #BRUHPLEASEWORK = Motor(Port.A)
    #BRUHPLEASEWORK.run_time(200, 10, then=Stop.HOLD, wait=True)
    #BRUHPLEASEWORK.run_target(500, 1000)
    #time.sleep(5)
    #BRUHPLEASEWORK.dc(100)
    #time.sleep(10)

#brickthing.motorright.run_angle(10, 20)
#brickthing.motorright.run_angle(10, -20)
#mainloop()

time.sleep(5)
mainloop()