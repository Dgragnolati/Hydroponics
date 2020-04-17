#Function to party
import json
import os
from datetime import datetime
import time
import threading

import RPi.GPIO as GPIO
# set shit up
GPIO.setmode(GPIO.BOARD)

#Read settings from JSON
def returninfo ():
    settings = json.load(open('data/settings.json'))
    return settings

#turn specific controls (relays) on for a set duration and then turn off
def control_on (pin,duration):
    print("turning on the control for pin " + str(pin))
    GPIO.output(pin, GPIO.HIGH)
    print("waiting for " + str(duration))
    time.sleep(duration)
    print("turn off the contorl")
    GPIO.output(pin, GPIO.LOW)


def test():
    print ("testing string no args")
#pumpkin time. If it is midnight, go ahead and schedules the days work

def schedule_events():
    current_settings = returninfo()
    for controls in current_settings:
        GPIO.setup(controls['pin'], GPIO.OUT)
        for events in current_settings[controls]['Start_Times']:
            print (str(datetime.strptime(events,"%H:%M")))
            delta_time = (datetime.strptime(events,"%H:%M") - (datetime.now()))
            print (str(delta_time.seconds))
            print ("Creating an event for " + controls + " @ " + events + " for " + current_settings[controls]['Duration'] + " Which is in " + str(delta_time))
            threading.Timer(delta_time.seconds,control_on,(current_settings[controls]['Pin'],int(current_settings[controls]['Duration']))).start()

schedule_events()
#GPIO.cleanup()
