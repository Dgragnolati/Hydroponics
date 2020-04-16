#Function to party
import time
import RPi.GPIO as GPIO

# set shit up
GPIO.setmode(GPIO.BOARD)

#set Pump #4 (AKA WHITE LED (Schematic)
Pump_Pin = 7
#set Lights #17 (AKA BLUE LED (Schematic)
Lamp_Pin = 11
# SET outputs
GPIO.setup(Pump_Pin, GPIO.OUT)
GPIO.setup(Lamp_Pin, GPIO.OUT)


#Read setting from JSON

#not sure if there should be a dic or not on this like a Pump (Start, End, Start End etc )

#set time pump on
#set duration of pump

#set time light on
#set time

#Loop waiting for the correc time to turn thing on

#pump on funciton
#pump off function

#lights on funciton
#light off function

#test script

GPIO.output(Pump_Pin, GPIO.HIGH)
GPIO.output(Pump_Pin, GPIO.HIGH)

time.sleep(5)

GPIO.output(Pump_Pin, GPIO.LOW)
GPIO.output(Pump_Pin, GPIO.LOW)

GPIO.cleanup()
