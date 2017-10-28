import RPi.GPIO as GPIO

class pir_sensor:
    # describes the type
    typeDescription = 'PIR Sensor'

    def __init__(self):
        self.sensor_input_pin = 5
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sensor_input_pin, GPIO.IN)

    def get_reading(self):
        # NOTE - the PIR sensor will return True for 10 seconds!
        if GPIO.input(self.sensor_input_pin):
            return True
        else:
            return False


import time
pir_sensor = pir_sensor()

try:
	print ("PIR Module Test (CTRL+C to exit)")
	time.sleep(2)
	print ("Ready")
	while True:
            if pir_sensor.get_reading():
                # NOTE - the PIR sensor will return True for 10 seconds!
                print("Works! waiting for 10 seconds for PIR alert to close")
                time.sleep(10)
except KeyboardInterrupt:
	print (" Quit")
	GPIO.cleanup()





