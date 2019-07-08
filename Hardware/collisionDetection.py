#!/usr/bin/python
import RPi.GPIO as GPIO
import time

while True:
    try:

        GPIO.setmode(GPIO.BOARD)

        PIN_TRIGGER = 13
        PIN_ECHO = 15

        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        #Resetting sensor
        time.sleep(2)

        #Calculate the distance
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

        #Output sensor distance
        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)

        #This will be interconnected to the motor controls
        #in order to prevent object collisions.
        print("Distance:",distance,"cm")

    finally:
        GPIO.cleanup()
