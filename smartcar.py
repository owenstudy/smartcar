#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 4/5/2021 8:39 AM
# @Author  : Owen_study
# @Email   : owen_study@126.com
# @File    : smartcar.py
# @Software: PyCharm
# ===============================================
import RPi.GPIO as GPIO                     #引入RPi.GPIO库函数命名为GPIO
import time                                 #引入计时time函数

def car_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2,GPIO.OUT)
    GPIO.setup(3,GPIO.OUT)
    GPIO.setup(4,GPIO.OUT)

    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(20,GPIO.OUT)
    GPIO.setup(21,GPIO.OUT)
    GPIO.setwarnings(False)

# 前进
def forward(sleep_time):
    GPIO.output(2,True)
    GPIO.output(3,True)
    GPIO.output(4,False)

    GPIO.output(16,True)
    GPIO.output(20,True)
    GPIO.output(21,False)
    time.sleep(sleep_time)
# 停止运行
def stop(sleep_time):
    GPIO.output(2,False)
    GPIO.output(3,True)
    GPIO.output(4,False)

    GPIO.output(16,False)
    GPIO.output(20,True)
    GPIO.output(21,False)
    time.sleep(sleep_time)


# auto run
def autorun():
    run_times = 0
    while run_times<10:
        forward(3)
        stop(3)
        run_times = run_times + 1
# time.sleep(5)
# GPIO.clearup()

if __name__ == '__main__':
    autorun()
    pass
