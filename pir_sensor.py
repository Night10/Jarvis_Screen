import RPi.GPIO as GPIO

class pir_sensor:
    # describes the type
    typeDescription = 'PIR Sensor'

    def __init__(self):
        self.sensor_input_pin = 6
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.sensor_input_pin, GPIO.IN)

    def get_reading(self):
        # NOTE - the PIR sensor will return True for 10 seconds!
        if GPIO.input(self.sensor_input_pin):
            return True
        else:
            return False
