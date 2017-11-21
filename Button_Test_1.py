import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:

    if GPIO.input(33) == False:
        print('Button Pressed 33...')
        time.sleep(0.2)
    elif GPIO.input(31) == False:
        print('Button Pressed 31...')
        time.sleep(0.2)
    elif GPIO.input(32) == False:
        print('Button Pressed 32...')
        time.sleep(0.2)
    elif GPIO.input(29) == False:
        print('Button Pressed 29...')
        time.sleep(0.2)