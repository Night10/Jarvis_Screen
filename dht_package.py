import Adafruit_DHT
import requests

class dht_package:
    typeDescription = 'Sends a DHT Package to Jarvis Brain'

    def __init__(self):
        self.jarvis_brain_endpoint = "http://jarvis_brain:5000/"
        self.jarvis_brain_heartbeat = "/heartbeat"
        self.jarvis_brain_post_dht = "InternalComms/CollectDHT/"
        self.jarvis_brain_collect_dht = "ExternalComms/getLast7DaysTemperature/"
        self.sensor = Adafruit_DHT.DHT11
        self.sensor_pin = 6
        self.dht_package_shape = {}
        self.dht_package_shape["temp"] = -1
        self.dht_package_shape["humi"] = -1
        self.dht_package_shape["voltage"] = -1
        self.dht_package_shape["location"] = "House/"
        self.dht_package_shape["message"] = "Initialised"
        self.dht_package_post_response = ""
        self.dht_collection = []

    def get_reading(self):
        try:
            humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.sensor_pin)
            self.dht_package_shape["temp"] = temperature
            self.dht_package_shape["humi"] = humidity
            self.dht_package_shape["message"] = ""
            return True
        except:
            print("errored collecting temperature")
            return False

    def ship_reading(self):
        if self.get_reading():
            postData = '{'
            postData += '"Temperature":"'+str(self.dht_package_shape["temp"])+'",'
            postData += '"Humidity":"'+str(self.dht_package_shape["humi"])+'",'
            postData += '"BatteryLevel":"'+str(self.dht_package_shape["voltage"])+'",'
            postData += '"Location":"'+self.dht_package_shape["location"]+'",'
            postData += '"InternalComms.Name":"DHT Temperature Package",'
            postData += '"InternalComms.Received":"",'
            postData += '"InternalComms.Sent":"",'
            postData += '"InternalComms.State":"Sent",'
            postData += '"InternalComms.Message":"'+self.dht_package_shape["message"]+'"}'
            url = self.jarvis_brain_endpoint + self.jarvis_brain_post_dht
            headers = {'content-type': 'application/json'}
            try:
                resp = requests.post(url, data=postData, headers=headers)
                self.dht_package_post_response = resp.reason
                return True
            except (requests.ConnectionError):
                print("something went wrong sending the data to Jarvis Brain")
                return False

    def collect_readings(self, location):
        if location is not None:
            raw_collection = requests.get(self.jarvis_brain_endpoint + self.jarvis_brain_collect_dht + location)
            self.dht_collection = raw_collection.json()

    def get_latest_temperature(self, location):
        if location is not None:
            self.collect_readings(location)
            readings = self.dht_collection
            return readings[0]

    def get_lowest_garden_temperature(self):
        readings = self.get_latest_temperature("Garden/")
        # TODO - convert the set into a date ordered collection
        #        and cut the lowest in the last 24 hours
