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
    GPIO.output(20,False)
    GPIO.output(21,True)
    time.sleep(sleep_time)
# 原地转圈圈
def circle(sleep_time):
    GPIO.output(2,True)
    GPIO.output(3,True)
    GPIO.output(4,False)

    GPIO.output(16,True)
    GPIO.output(20,False)
    GPIO.output(21,True)
    time.sleep(sleep_time)
# 后退
def backward(sleep_time):
    GPIO.output(2,True)
    GPIO.output(3,False)
    GPIO.output(4,True)

    GPIO.output(16,True)
    GPIO.output(20,True)
    GPIO.output(21,False)
    time.sleep(sleep_time)
# 停止运行
def stop(sleep_time):
    GPIO.output(2,True)
    GPIO.output(3,False)
    GPIO.output(4,False)

    GPIO.output(16,True)
    GPIO.output(20,False)
    GPIO.output(21,False)
    time.sleep(sleep_time)

# auto run
def autorun():
    run_times = 0
    car_init()
    while run_times<10:
        forward(1)
        stop(2)
        circle(2)
        stop(2)
        backward(1)
        run_times = run_times + 1
# time.sleep(5)
# GPIO.clearup()

if __name__ == '__main__':
    autorun()
    pass
