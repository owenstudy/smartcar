#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 4/5/2021 7:26 PM
# @Author  : Owen_study
# @Email   : owen_study@126.com
# @File    : supersoundwave.py
# @Software: PyCharm
# ===============================================
import RPi.GPIO as GPIO                     #引入RPi.GPIO库函数命名为GPIO
import time                                 #引入计时time函数

# 使用超声波检查距离
def checkdistince():
    # GPIO 23, trigger
    # GPIO 24, echo
    # 初始化
    # GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
    # GPIO.setup(24, GPIO.IN)
    # 发出触发信号
    GPIO.output(23, GPIO.HIGH)
    # 保持15us的超声波发射，避免能量太低无法返回
    time.sleep(0.000030)
    # 停止发射超声波
    GPIO.output(23, GPIO.LOW)
    while not GPIO.input(24):
        pass
    # 发现高电平时开时计时
    t1 = time.time()
    # 如果有检测到反射返回的超声波，那么就持续计时，否则就跳出循环，计时结束
    while GPIO.input(24):
        pass
    # 高电平结束停止计时
    t2 = time.time()
    # 返回距离，单位为米
    return (t2 - t1) * 340 / 2




if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    # GPIO.setup(23,GPIO.OUT,initial=GPIO.LOW)
    # GPIO.setup(24,GPIO.IN)
    # time.sleep(2)
    try:
        while True:
            distince = 'distince :{0} m'.format(checkdistince())
            print(distince)
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.clearup()
    pass
