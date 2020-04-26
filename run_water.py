#Function
from datetime import datetime
import RPi.GPIO as GPIO
import time
# set up GPIO
GPIO.setmode(GPIO.BOARD)
#turn specific controls (relays) on for a set duration and then turn off
def control_on (pin,duration):
    print("setting up GPIO Pin")
    GPIO.setup(pin, GPIO.OUT)
    print("turning on the control for pin " + str(pin))
    GPIO.output(pin, GPIO.HIGH)
    print("waiting for " + str(duration))
    time.sleep(duration)
    print("turn off the contorl")
    GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()

control_on(16,600)
