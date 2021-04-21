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
        print('distinct: {0}'.format(distance))
        # 距离小于0.5米时右转
        while distance<0.5:
            run('CL',15,0.02)
            time.sleep(0.1)
            distance = supersoundwave.checkdistince()
            print('distinct: {0}'.format(distance))
            time.sleep(0.2)
        # 安全距离内前行
        run('FW', 30, 0.5)
        run_times = run_times +1

def test_pwm():
    car_init()
    autorun_supersoundwave()
    # run('FW',30,1)
    # run('BW',50,1)
    # run('TL',20,1)
    # run('TR',60,2)
#speed, 速度的百分比，如10代表按最高速度的10%运行，run_time 运行时间，单位为秒
def forward_pwm(speed, run_time):
    # 前进
    GPIO.output(wheel_gpio_left_1, GPIO.LOW)
    GPIO.output(wheel_gpio_left_2, GPIO.HIGH)
    GPIO.output(wheel_gpio_right_1, GPIO.LOW)
    GPIO.output(wheel_gpio_right_2, GPIO.HIGH)

    pwm_left = GPIO.PWM(wheel_gpio_left_enable, 320)
    pwm_right = GPIO.PWM(wheel_gpio_right_enable, 320)
    pwm_left.start(speed)
    pwm_right.start(speed)
    time.sleep(run_time)
    pwm_left.stop()
    pwm_right.stop()
    pass
#speed, 速度的百分比，如10代表按最高速度的10%运行，run_time 运行时间，单位为秒
# run_mode，运行方向，前进 FW，后退BW，左转TL，右转TR, CL-circle 原地转圈, SP-stop
def run(run_mode, speed, run_time):
    if run_mode == 'FW':
        # 前进
        GPIO.output(wheel_gpio_left_1, GPIO.HIGH)
        GPIO.output(wheel_gpio_left_2, GPIO.LOW)
        GPIO.output(wheel_gpio_right_1, GPIO.HIGH)
        GPIO.output(wheel_gpio_right_2, GPIO.LOW)
    elif run_mode == 'BW':
        # 后退
        GPIO.output(wheel_gpio_left_1, GPIO.LOW)
        GPIO.output(wheel_gpio_left_2, GPIO.HIGH)
        GPIO.output(wheel_gpio_right_1, GPIO.LOW)
        GPIO.output(wheel_gpio_right_2, GPIO.HIGH)
    elif run_mode == 'TL':
        # 左转
        GPIO.output(wheel_gpio_left_1, GPIO.LOW)
        GPIO.output(wheel_gpio_left_2, GPIO.LOW)
        GPIO.output(wheel_gpio_right_1, GPIO.HIGH)
        GPIO.output(wheel_gpio_right_2, GPIO.LOW)
    elif run_mode == 'TR':
        # 右转
        GPIO.output(wheel_gpio_left_1, GPIO.HIGH)
        GPIO.output(wheel_gpio_left_2, GPIO.LOW)
        GPIO.output(wheel_gpio_right_1, GPIO.LOW)
        GPIO.output(wheel_gpio_right_2, GPIO.LOW)
    elif run_mode == 'CL':
        # 原地转圈
        GPIO.output(wheel_gpio_left_1, GPIO.HIGH)
        GPIO.output(wheel_gpio_left_2, GPIO.LOW)
        GPIO.output(wheel_gpio_right_1, GPIO.LOW)
        GPIO.output(wheel_gpio_right_2, GPIO.HIGH)
    elif run_mode == 'SP':
        # 停止
        GPIO.output(wheel_gpio_left_1, GPIO.LOW)
        GPIO.output(wheel_gpio_left_2, GPIO.LOW)
        GPIO.output(wheel_gpio_right_1, GPIO.LOW)
        GPIO.output(wheel_gpio_right_2, GPIO.LOW)

    pwm_left = GPIO.PWM(wheel_gpio_left_enable, 320)
    pwm_right = GPIO.PWM(wheel_gpio_right_enable, 320)
    pwm_left.start(speed)
    pwm_right.start(speed)
    time.sleep(run_time)
    pwm_left.stop()
    pwm_right.stop()
    pass
def autorun_pwm():
    car_init()
    # forward(0.5)
    # stop(1)
    # GPIO.setmode(GPIO.BCM)
    GPIO.output(wheel_gpio_left_1,GPIO.LOW)
    GPIO.output(wheel_gpio_left_2,GPIO.HIGH)
    GPIO.output(wheel_gpio_right_1,GPIO.LOW)
    GPIO.output(wheel_gpio_right_2,GPIO.HIGH)

    pwm_pin_left = wheel_gpio_left_enable
    pwm_pin_right = wheel_gpio_right_enable
    GPIO.setup(pwm_pin_left, GPIO.OUT)  # 使能gpio口为输出
    GPIO.setup(pwm_pin_right, GPIO.OUT)  # 使能gpio口为输出
    pwm_left = GPIO.PWM(pwm_pin_left, 320)
    pwm_right = GPIO.PWM(pwm_pin_right, 320)
    for i in range(10,100):
        pwm_left.start(i)
        pwm_right.start(i)
        print('ok')
        time.sleep(0.1)
    for j in range(100,10, -1):
        print('yes')
        pwm_left.start(j)
        pwm_right.start(j)
        time.sleep(0.1)
    pwm_left.stop()
    pwm_right.stop()
    # GPIO.cleanup()
    pass
def test_car():
    # pwm test
    autorun_pwm()
    # run_times = 0
    # car_init()
    # autorun_supersoundwave()
    # while run_times<5:
    #     turn_left(1)
    #     run_times = run_times +1
    # stop(1)
    # run_times = 0
    # while run_times<10:
    #     turn_right(1)
    #     run_times = run_times +1
    # stop(1)

# time.sleep(5)
# GPIO.clearup()

if __name__ == '__main__':
    # autorun()
    test_pwm()
    pass
