import RPi.GPIO as GPIO

class transistor_switch:
    # describes the type
    typeDescription = 'Transistor Switch on pin 13 - initally set to on'

    def __init__(self):
        self.switch_pin = 13
        self.switch_state = True
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.switch_pin, GPIO.OUT)

    def switch(self, switch_state):
        if switch_state is not None:
            self.switch_state = switch_state
            GPIO.output(self.switch_pin, self.switch_state)
            return self.switch_state

import time
screen = transistor_switch()
screen.switch(True)
print(screen.switch_state)
time.sleep(3)
screen.switch(False)
print(screen.switch_state)
time.sleep(3)
screen.switch(True)
print(screen.switch_state)
time.sleep(3)
GPIO.cleanup()