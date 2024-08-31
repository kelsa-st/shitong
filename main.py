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
    value = int(500 + (angle / 180.0) * 2000)
    servo.duty_ns(value * 1000) # 设置PWM占空比

def set_motor_speed(speed=1023, direction=1):
    motor.duty(speed)
    motor_dir.value(direction) # 设置电机方向，1为前进，0为后退

def go_forward(speed=1023, duration=5):
    set_motor_speed(speed, direction=1)
    set_servo_angle(90) # 保持直行
    time.sleep(duration)

def turn_right():
    set_servo_angle(135) # 向右转弯
    time.sleep(1) # 保持转弯一段时间
    set_servo_angle(90) # 返回直行

def turn_left():
    set_servo_angle(45) # 向左转弯
    time.sleep(1) # 保持转弯一段时间
    set_servo_angle(90) # 返回直行

def stop():
    motor.duty(0) # 停止电机
    motor_dir.value(0) # 设置电机方向为低电平
    set_servo_angle(90) # 将舵机角度设置为直行（90度）
    time.sleep(1) # 确保小车停止
    print("Car stopped.")

    # 让小车跑一个大大的长方形然后停止
go_forward(duration=10) # 前进10秒（长边）
turn_right() # 右转
go_forward(duration=5) # 前进5秒（短边）
turn_right() # 右转
go_forward(duration=10) # 前进10秒（长边）
turn_right() # 右转
go_forward(duration=5) # 前进5秒（短边）
turn_right() # 右转
stop()

