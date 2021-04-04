#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 4/4/2021 10:33 AM
# @Author  : Owen_study
# @Email   : owen_study@126.com
# @File    : cartest.py
# @Software: PyCharm
# ===============================================
import RPi.GPIO as GPIO                     #引入RPi.GPIO库函数命名为GPIO
import time                                 #引入计时time函数

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)

GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setwarnings(False)

GPIO.output(2,True)
GPIO.output(3,True)
GPIO.output(4,False)

GPIO.output(16,True)
GPIO.output(20,True)
GPIO.output(21,False)

time.sleep(5)
# GPIO.clearup()

if __name__ == '__main__':
    pass
