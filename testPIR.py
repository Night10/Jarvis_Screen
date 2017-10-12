import RPi.GPIO as GPIO

class pir_sensor:
    # describes the type
    typeDescription = 'PIR Sensor'

    def __init__(self):
        self.sensor_input_pin = 13
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(self.sensor_input_pin, GPIO.IN) # Read output from PIR motion sensor

    def get_reading(self):
        i=GPIO.input(13)
        if i==0:          # When output from motion sensor is LOW
            return False
        elif i==1:        # When output from motion sensor is HIGH
            return True
