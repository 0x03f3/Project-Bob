import Rpi.GPIO as gpio
import time

def init():

    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)

def forward(tf):

    init()
    gpio.output (7, True)
    gpio.output (11, True)
    time.sleep(tf) '
    gpio.cleanup()

forward(1)

def reverse(tf):

    init()
    gpio.output (7, False)
    gpio.output (11, True)
    time.sleep(tf)
    gpio.cleanup()


reverse(1)

def turn_left(tf):

    init()

    gpio.output (7, True)
    gpio.output (11, False)
    time.sleep(tf)
    gpio.cleanup()

turn_left(1)

def turn_right(tf):

    init()
    gpio.output (7, False)
    gpio.output (11, True)
    time.sleep(tf)
    gpio.cleanup()

turn_right(1)
