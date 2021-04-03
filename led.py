#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 4/3/2021 7:18 PM
# @Author  : Owen_study
# @Email   : owen_study@126.com
# @File    : led.py
# @Software: PyCharm
# ===============================================

import RPi.GPIO as GPIO                     #引入RPi.GPIO库函数命名为GPIO
import time                                 #引入计时time函数
# BOARD编号方式，基于插座引脚编号
GPIO.setmode(GPIO.BOARD)                    #将GPIO编程方式设置为BOARD模式
# 输出模式
GPIO.setup(11, GPIO.OUT)                    #将GPIO引脚11设置为输出引脚

while True:                                 # 条件为真，下面程序一直循环执行
        GPIO.output(11, GPIO.HIGH)          #将11引脚电压置高，点亮LED灯
        time.sleep(1)                       #延时1秒
        GPIO.output(11, GPIO.LOW)           #将11引脚电压置低，熄灭LED灯
        time.sleep(1)                       #延时1秒
if __name__ == '__main__':
    pass
