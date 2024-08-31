from machine import Pin, PWM
import time

    # 定义舵机和电机的PWM引脚
SERVO_PIN = 5 # 舵机连接的引脚 (GPIO 5)
MOTOR_PIN = 14 # 电机连接的引脚 (GPIO 15)
MOTOR_DIR_PIN = 12 # 电机方向引脚 (GPIO 13)

    # 初始化舵机
servo = PWM(Pin(SERVO_PIN), freq=50) # 50Hz 适用于大多数舵机
   # 初始化电机
motor = PWM(Pin(MOTOR_PIN), freq=1000) # 1000Hz 适用于控制电机的PWM频率
motor_dir = Pin(MOTOR_DIR_PIN, Pin.OUT) # 设置电机方向引脚

def set_servo_angle(angle):
    # 将角度转换为PWM占空比 (500-2500微秒之间)
    value = int(500 + (angle / 180.0) * 2000)
    servo.duty_ns(value * 1000) # 设置PWM占空比

def set_motor_speed(speed=1023, direction=1):
    # speed 应该在0（停止）到1023（最大速度）之间
    motor.duty(speed)
    motor_dir.value(direction) # 设置电机方向，1为前进，0为后退

def go_forward_in_circle(duration, speed=1023):
    set_motor_speed(speed, direction=1) # 设置速度并前进
    set_servo_angle(110) # 舵机角度设置为120度，使小车以圆形轨道行驶
    time.sleep(duration) # 持续行驶给定时间

def stop():
    print("Stopping the car...")
    motor.duty(0)
    motor_dir.value(0)
    set_servo_angle(90)
    time.sleep(1)
    print("Car should be stopped now.")
    
    # 让小车跑一个圆形20秒，然后停止
go_forward_in_circle(20)
stop()

import main