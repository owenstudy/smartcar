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
import supersoundwave

# 左轮总控制
wheel_gpio_left_enable = 2
# 左前轮
wheel_gpio_left_1 =3
# 左后轮
wheel_gpio_left_2 =4

# 右轮总控制
wheel_gpio_right_enable = 16
# 右前轮
wheel_gpio_right_1 = 20
# 右后轮
wheel_gpio_right_2 = 21

# 超声波GPIO trigger端口
supersound_gpio_trigger = 23
# 超声波echo 端口
supersound_gpio_echo = 24



def car_init():
    # 左边的两个轮子
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(wheel_gpio_left_enable,GPIO.OUT)
    GPIO.setup(wheel_gpio_left_1,GPIO.OUT)
    GPIO.setup(wheel_gpio_left_2,GPIO.OUT)
    # 右边的两个轮子
    GPIO.setup(wheel_gpio_right_enable,GPIO.OUT)
    GPIO.setup(wheel_gpio_right_1,GPIO.OUT)
    GPIO.setup(wheel_gpio_right_2,GPIO.OUT)
    GPIO.setwarnings(False)

    # super sound wave
    GPIO.setup(supersound_gpio_trigger,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(supersound_gpio_echo,GPIO.IN)
    time.sleep(2)


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
# 左转
def turn_left(sleep_time):
    GPIO.output(wheel_gpio_left_enable,True)
    GPIO.output(wheel_gpio_left_1,False)
    GPIO.output(wheel_gpio_left_2,False)

    GPIO.output(wheel_gpio_right_enable,True)
    GPIO.output(wheel_gpio_right_1,False)
    GPIO.output(wheel_gpio_right_2,True)
    time.sleep(sleep_time)
# 左转
def turn_right(sleep_time):
    GPIO.output(wheel_gpio_left_enable,True)
    GPIO.output(wheel_gpio_left_1,True)
    GPIO.output(wheel_gpio_left_2,False)

    GPIO.output(wheel_gpio_right_enable,True)
    GPIO.output(wheel_gpio_right_1,False)
    GPIO.output(wheel_gpio_right_2,False)
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

def test_car():
    run_times = 0
    car_init()
    while run_times<5:
        turn_left(1)
        run_times = run_times +1
    stop(1)
    run_times = 0
    while run_times<10:
        turn_right(1)
        run_times = run_times +1
    stop(1)
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
# auto run with supersoundwave
def autorun_supersoundwave():
    run_times = 0
    car_init()
    while run_times<10:
        distance = supersoundwave.checkdistince()
        # 距离小于0.5米时右转
        while distance<0.5:
            pass



# time.sleep(5)
# GPIO.clearup()

if __name__ == '__main__':
    # autorun()
    test_car()
    pass
