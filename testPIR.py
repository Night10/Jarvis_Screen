import RPi.GPIO as GPIO

class pir_sensor:
    # describes the type
    typeDescription = 'PIR Sensor'

    def __init__(self):
        self.sensor_input_pin = 5
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sensor_input_pin, GPIO.IN)

        # GPIO.setmode(GPIO.BCM)
        # PIR_PIN = 7
        # GPIO.setup(PIR_PIN, GPIO.IN)
    def get_reading(self):
        if GPIO.input(self.sensor_input_pin):
            return True
        else:
            return False


# import time
# pir_sensor = pir_sensor()

# try:
# 	print ("PIR Module Test (CTRL+C to exit)")
# 	time.sleep(2)
# 	print ("Ready")
# 	while True:
#             if pir_sensor.get_reading():
#                 print("Works!")
#                 time.sleep(1)
# except KeyboardInterrupt:
# 	print (" Quit")
# 	GPIO.cleanup()


