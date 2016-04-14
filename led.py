import RPi.GPIO as GPIO
import time

GPIO_PIN = 12
DEBUG = 1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(GPIO_PIN, GPIO.OUT)
GPIO.output(GPIO_PIN, GPIO.LOW)

while True:
    print 'on'
    GPIO.output(GPIO_PIN, GPIO.HIGH)
    time.sleep(1)

    print 'off'
    GPIO.output(GPIO_PIN, GPIO.LOW)
    time.sleep(1)
