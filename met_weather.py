import urllib.request, urllib.parse, urllib.error, json, time, gettime, collections, gettime
from urllib.request import urlopen

class met_weather:
    # describes the type
    typeDescription = 'Gets the Weather from the MET Office with the location name'

    # Setting an immutable default value
    # http://stackoverflow.com/questions/2681243/how-should-i-declare-default-values-for-instance-variables-in-python

    def __init__(self, alert_message, weatherLocationName='Amesbury'):
        self.last_collected = gettime.get_time_now()
        self.weatherLocationName = weatherLocationName
        self.result = {'System': {}, 'Weather': {}}
        self.result['System']['Result'] = True
        self.result['System']['Error'] = collections.OrderedDict()
        self.result['Weather']['Now'] = collections.OrderedDict()
        self.result['Weather']['Later'] = collections.OrderedDict()
        self.result['Weather']['Days'] = collections.OrderedDict()
        self.temporary_weather = {}
        self.alert_message = alert_message

        # Get the main weather
        self.get_weather()
        
    def get_weather(self):
        if (self.weatherLocationName == 'Amesbury'):
            weather_url = 'http://boncester.serveftp.com/projects/jarvis/getWeather.php'
            # weather_url = 'http://127.0.0.1/getWeather.php'
        if not weather_url:
            self.return_error("Weather URL is an empty string")
            return False 

        try:
            response = urlopen(weather_url)
        except except urllib.error.URLError as e:
            self.alert_message.add_message("Error of: " + r.reason + " at: " + gettime.get_time_now(), 15)
        else:
            data = response.read().decode("utf-8")
            weather_data = json.loads(data)

            for weather_dataKey, weather_dataValue in list(weather_data.items()):
                if weather_dataKey == "System":
                    for systemKey, systemValue in list(weather_dataValue.items()):
                        self.result['System'][systemKey] = systemValue

                elif weather_dataKey == "Weather":
                    for weatherKey, weatherValue in list(weather_dataValue.items()):
                        self.temporary_weather[weatherKey] = weatherValue
            self.last_collected = gettime.get_time_now()
            self.alert_message.add_message("MET at: " + self.last_collected, 15)

    def show_days(self):
        if not self.temporary_weather:
            self.return_error("Temporary data contains no rows")
        return False

    def get_weather_now(self):
        if not self.temporary_weather:
            self.return_error("Temporary data contains no rows")
            return False

        todays_date = time.strftime("%Y-%m-%dZ")

        for day in sorted(self.temporary_weather['Days']):
            if day.upper() == todays_date:
                unordered_weather_later = {}

                todays_weather_data = self.temporary_weather['Days'][day.upper()]

                for weather_row in todays_weather_data:
                    total_minutes_today = int(time.strftime('%H')) * 60 + int(time.strftime('%M'))
                    if total_minutes_today > int(weather_row['$']) and total_minutes_today < int(weather_row['$']) + 180:
                        # Weather NOW
                        for weather_now_key, weather_now_value in weather_row.items():
                            if(weather_now_key != '$'):
                                weather_description = self.temporary_weather['Params'][weather_now_key]['Description']
                                weather_units = self.temporary_weather['Params'][weather_now_key]['Units']
                                self.result['Weather']['Now'][weather_now_key] = [ weather_description, weather_now_value + ' ' + weather_units ]

                    elif total_minutes_today < int(weather_row['$']):
                        # Weather Later Today
                        start_hour = ""
                        end_hour = ""
                        am_pm = "am"
                        if int(weather_row['$']) / 60 <= 12:
                            start_hour = "%d" % (int(weather_row['$']) / 60)
                        else:
                             start_hour = "%d" % (int(weather_row['$']) / 60 / 2)
                             am_pm = "pm"
                        if (int(int(weather_row['$']) + 180) / 60) <= 12:
                            end_hour = "%d" % (int(int(weather_row['$']) + 180) / 60)
                        else:
                             end_hour = "%d" % (int(int(weather_row['$']) + 180) / 60 / 2)
                             am_pm = "pm"

                        future_time = "%s-%s %s" % (start_hour, end_hour, am_pm)
                        self.result['Weather']['Later'][future_time] = {}
                        for weather_now_key, weather_now_value in list(weather_row.items()):
                            
                            self.result['Weather']['Later'][future_time][weather_now_key] = weather_now_value

            else:
                for weather_row in self.temporary_weather['Days'][day.upper()]:
                    for weather_day_key, weather_day_value in list(weather_row.items()):
                        if weather_day_key == '$' and weather_day_value == '720':
                            day_name = gettime.convert_zulu_to_dayname(day)
                            self.result['Weather']['Days'][day_name] = weather_row 

    def return_error(self, error_message):
        self.result['System']['Success'] = False
        self.result['System']['Error'] = error_message

    def format_weather_now(self):
        weather = {}
        for weather_dataKey, weather_dataValue in list(self.result['Weather']['Now'].items()):
            weather[weather_dataKey] = weather_dataValue

        return weather

    def format_weather_later(self):
        return self.result['Weather']['Later']

    def format_future_days(self):
        return self.result['Weather']['Days']
