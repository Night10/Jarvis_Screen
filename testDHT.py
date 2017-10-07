#import RPi.GPIO as GPIO

# Sets the GPIO numbering to PI GPIO recognisable numbering
#GPIO.setmode(GPIO.BOARD)

# Assign the DHT module to pin 6
#GPIO.setup(channel, GPIO.IN)

import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
pin = 6
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
