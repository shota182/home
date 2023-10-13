#!/usr/bin/env python3

import RPi.GPIO as GPIO # RPi.GPIOモジュールを使用
import time
import sys

args = sys.argv
duty = int(args[1])
if(duty < 0 or duty > 100): sys.exit()

# LEDとスイッチのGPIO番号
# デフォルトはRPZ-IR-Sensorの緑LEDと赤SW
# 必要に応じて変更
gpio_pwm = 2
gpio_sw = 5

# GPIO番号指定の準備
GPIO.setmode(GPIO.BCM)

# LEDピンを出力に設定
GPIO.setup(gpio_pwm, GPIO.OUT)

pi = GPIO.PWM (gpio_pwm, 50 )  #( pin, Hz )
pi.start ( 0 )

try:
    while True: pi.ChangeDutyCycle( duty )
except KeyboardInterrupt: pass

p0.stop()
GPIO.cleanup()
