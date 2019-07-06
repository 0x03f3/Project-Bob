#GPIO Pin test via the LED test board.

from gpiozero import LED
from time import sleep

pin = int(input("Enter test pin: "))

led = LED(pin)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
