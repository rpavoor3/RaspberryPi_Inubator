from gpiozero import DigitalOutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
import time

x = DigitalOutputDevice(21)

while(1):
    x.off()
    time.sleep(1)
    print("Running...")