import RPi.GPIO as GPIO

class transistor_switch:
    # describes the type
    typeDescription = 'Transistor Switch on pin 13 - initally set to on'

    def __init__(self):
        self.switch_pin = 13
        self.switch_state = True
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.switch_pin, GPIO.OUT)

    def switch(self, switch_state):
        if switch_state is not None:
            self.switch_state = switch_state
            GPIO.output(self.switch_pin, self.switch_state)
            return self.switch_state

