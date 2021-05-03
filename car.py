#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 5/3/2021 8:02 PM
# @Author  : Owen_study
# @Email   : owen_study@126.com
# @File    : car.py
# @Software: PyCharm
# ===============================================
import RPi.GPIO as GPIO                     #引入RPi.GPIO库函数命名为GPIO
import time                                 #引入计时time函数
import supersoundwave

class Car( object ):
    # initial for parameters
    def __init__(self):
        # 左轮总控制
        self.wheel_gpio_left_enable = 2
        # 左前轮
        self.wheel_gpio_left_1 = 3
        # 左后轮
        self.wheel_gpio_left_2 = 4

        # 右轮总控制
        self.wheel_gpio_right_enable = 16
        # 右前轮
        self.wheel_gpio_right_1 = 20
        # 右后轮
        self.wheel_gpio_right_2 = 21

        # 超声波GPIO trigger端口
        self.supersound_gpio_trigger = 23
        # 超声波echo 端口
        self.supersound_gpio_echo = 24
        # 左边的两个轮子
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.wheel_gpio_left_enable, GPIO.OUT)
        GPIO.setup(self.wheel_gpio_left_1, GPIO.OUT)
        GPIO.setup(self.wheel_gpio_left_2, GPIO.OUT)
        # 右边的两个轮子
        GPIO.setup(self.wheel_gpio_right_enable, GPIO.OUT)
        GPIO.setup(self.wheel_gpio_right_1, GPIO.OUT)
        GPIO.setup(self.wheel_gpio_right_2, GPIO.OUT)
        GPIO.setwarnings(False)

        # super sound wave
        GPIO.setup(self.supersound_gpio_trigger, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.supersound_gpio_echo, GPIO.IN)
        time.sleep(2)
    # car initilize
    def car_init(self):
        # 左边的两个轮子
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.wheel_gpio_left_enable, GPIO.OUT)
        GPIO.setup(self.wheel_gpio_left_1, GPIO.OUT)
        GPIO.setup(self.wheel_gpio_left_2, GPIO.OUT)
        # 右边的两个轮子
        GPIO.setup(self.wheel_gpio_right_enable, GPIO.OUT)
        GPIO.setup(self.wheel_gpio_right_1, GPIO.OUT)
        GPIO.setup(self.wheel_gpio_right_2, GPIO.OUT)
        GPIO.setwarnings(False)

        # super sound wave
        GPIO.setup(self.supersound_gpio_trigger, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.supersound_gpio_echo, GPIO.IN)
        time.sleep(2)
    #speed, 速度的百分比，如10代表按最高速度的10%运行，run_time 运行时间，单位为秒
    # run_mode，运行方向，前进 FW，后退BW，左转TL，右转TR, CL-circle 原地转圈, SP-stop
    def run(self, run_mode, speed, run_time):
        if run_mode == 'FW':
            # 前进
            GPIO.output(self.wheel_gpio_left_1, GPIO.HIGH)
            GPIO.output(self.wheel_gpio_left_2, GPIO.LOW)
            GPIO.output(self.wheel_gpio_right_1, GPIO.HIGH)
            GPIO.output(self.wheel_gpio_right_2, GPIO.LOW)
        elif run_mode == 'BW':
            # 后退
            GPIO.output(self.wheel_gpio_left_1, GPIO.LOW)
            GPIO.output(self.wheel_gpio_left_2, GPIO.HIGH)
            GPIO.output(self.wheel_gpio_right_1, GPIO.LOW)
            GPIO.output(self.wheel_gpio_right_2, GPIO.HIGH)
        elif run_mode == 'TL':
            # 左转
            GPIO.output(self.wheel_gpio_left_1, GPIO.LOW)
            GPIO.output(self.wheel_gpio_left_2, GPIO.LOW)
            GPIO.output(self.wheel_gpio_right_1, GPIO.HIGH)
            GPIO.output(self.wheel_gpio_right_2, GPIO.LOW)
        elif run_mode == 'TR':
            # 右转
            GPIO.output(self.wheel_gpio_left_1, GPIO.HIGH)
            GPIO.output(self.wheel_gpio_left_2, GPIO.LOW)
            GPIO.output(self.wheel_gpio_right_1, GPIO.LOW)
            GPIO.output(self.wheel_gpio_right_2, GPIO.LOW)
        elif run_mode == 'CL':
            # 原地转圈
            GPIO.output(self.wheel_gpio_left_1, GPIO.HIGH)
            GPIO.output(self.wheel_gpio_left_2, GPIO.LOW)
            GPIO.output(self.wheel_gpio_right_1, GPIO.LOW)
            GPIO.output(self.wheel_gpio_right_2, GPIO.HIGH)
        elif run_mode == 'SP':
            # 停止
            GPIO.output(self.wheel_gpio_left_1, GPIO.LOW)
            GPIO.output(self.wheel_gpio_left_2, GPIO.LOW)
            GPIO.output(self.wheel_gpio_right_1, GPIO.LOW)
            GPIO.output(self.wheel_gpio_right_2, GPIO.LOW)

        pwm_left = GPIO.PWM(self.wheel_gpio_left_enable, 320)
        pwm_right = GPIO.PWM(self.wheel_gpio_right_enable, 320)
        pwm_left.start(speed)
        pwm_right.start(speed)
        time.sleep(run_time)
        pwm_left.stop()
        pwm_right.stop()
        pass
    # auto run with supersoundwave
    def autorun_supersoundwave(self):
        run_times = 0
        self.car_init()
        while run_times<200:
            distance = supersoundwave.checkdistince()
            print('distinct: {0}'.format(distance))
            # 距离小于0.5米时右转
            while distance<0.5:
                self.run('CL',30,0.2)
                # time.sleep(0.1)
                distance = supersoundwave.checkdistince()
                print('distinct: {0}'.format(distance))
            # 安全距离内前行
            self.run('FW', 20, 0.2)
            run_times = run_times +1

if __name__ == '__main__':
    mycar = Car()
    # mycar.run('CL',30,1)
    mycar.autorun_supersoundwave()
    pass
