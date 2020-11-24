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
    def whileCheck(self):
        if (self.check() > 0.5):
            if (self.motorright.angle() > 45):
                print("OVERRIDE")
            else:
                self.motorright.run_angle(10, 10) #10 left
                print("TURNED THIS WAY")
        elif (self.check() < -0.5):
            if (self.motorright.angle() < -45):
                print("OVERRIDE")
            else:
                self.motorright.run_angle(10, -10) #-10 right
                print("TURNED THAT WAY")
        #brickthing.savefile.write("LEFT: %d | RIGHT: %d" % (brickthing.leftambient, brickthing.rightambient))'''
    def rapidcheck(self):
        while brickthing.check() > 1 or brickthing.check() < -1: #while True:
            brickthing.whileCheck()
        print(brickthing.check())
        print("BREAK")
        time.sleep(5)
brickthing = Parts()

def mainloop():
    while True:
        brickthing.rapidcheck()

#brickthing.motorright.run_angle(10, 20)
#brickthing.motorright.run_angle(10, -20)
mainloop()