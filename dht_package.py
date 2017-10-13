import Adafruit_DHT, getip, gettime

class dht_package:
    typeDescription = 'Sends a DHT Package to Jarvis Brain'

    def __init__(self):
        self.jarvis_brain_endpoint = "http://jarvis_brain:5000/InternalComms"
        self.jarvis_brain_heartbeat = "/heartbeat"
        self.jarvis_brain_post_dht = "/CollectDHT"
        self.sensor = Adafruit_DHT.DHT11
        self.sensor_pin = 6
        self.dht_package_shape = {}
        self.dht_package_shape["temp"] = -1
        self.dht_package_shape["humi"] = -1
        self.dht_package_shape["voltage"] = -1
        self.dht_package_shape["location"] = "House"
        self.dht_package_shape["message"] = "Initialised"
        self.dht_package_shape["IP"] = "0.0.0.0"

    def get_reading(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.sensor_pin)
        self.dht_package_shape["IP"] = getip().get_ip_address()
        self.dht_package_shape["temp"] = temperature
        self.dht_package_shape["humi"] = humidity
        self.dht_package_shape["message"] = "Collected at " + gettime().get_time_now()

    def ship_reading(self):
        
        return true

# dht_package = dht_package()
# print(dht_package.get_reading())

