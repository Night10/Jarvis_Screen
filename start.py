#!/usr/bin/python

# -*- coding: utf-8 -*-
import time, pygame, gettime, getip, met_weather, timecycle as timecycle
import alert_message, command_centre as command_centre, text_generator as text

# alert messaging
alert_message = alert_message.alert_message()

# met_Weather - passing in alert 
knowledge_METWeather = met_weather.met_weather(alert_message)

# Timecycle for METWeather
metWeatherTimecycle = timecycle.timecycle()
metWeatherTimecycle.force_alarm = True

# System Commands
commands = command_centre.command_centre()

pygame.init()
screen = pygame.display.set_mode((656, 416))
# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set the background to black
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 250))
 
clock = pygame.time.Clock()

weather_icon_data = ""
weather_temperature_data = ""
weather_rain_probability_data = ""
house_temperature_data = ""
weather_later = ""
weather_days = ""

# Define the character icon to weather type lookup
weather_types = {}
weather_types['NA'] = ')'
weather_types['0'] = '1'
weather_types['1'] = 'B'
weather_types['2'] = '4'
weather_types['3'] = 'H'
weather_types['4'] = ')'
weather_types['5'] = 'J'
weather_types['6'] = 'M'
weather_types['7'] = 'N'
weather_types['8'] = 'N'
weather_types['9'] = '7'
weather_types['10'] = 'Q'
weather_types['11'] = 'Q'
weather_types['12'] = 'Q'
weather_types['13'] = '8'
weather_types['14'] = 'R'
weather_types['15'] = 'R'
weather_types['16'] = '"'
weather_types['17'] = 'U'
weather_types['18'] = 'U'
weather_types['19'] = '$'
weather_types['20'] = 'X'
weather_types['21'] = 'X'
weather_types['22'] = '#'
weather_types['23'] = 'W'
weather_types['24'] = 'W'
weather_types['25'] = 'W'
weather_types['26'] = 'W'
weather_types['27'] = 'W'
weather_types['28'] = '&'
weather_types['29'] = 'P'
weather_types['30'] = 'O'

# Define Fonts
font_weather_icons = ['meteocons', 'meteoconsregular']
font_standard = ['helveticaneue', 'texgyreheros']


def get_screen_height():
    x, y = screen.get_size()
    return y

def get_width(this):
    x, y = this.get_size()
    return x

def get_height(this):
    x, y = this.get_size()
    return y

def get_screen_width():
    x, y = screen.get_size()
    return x


def get_weather(weather_icon_data, weather_temperature_data, weather_rain_probability_data, house_temperature_data, weather_later, weather_days, alert_message):
    weather_now = False
    weather_later = False
    weather_days = False

    knowledge_METWeather.get_weather_now()
    # Format the now weather to something nice
    weather_now = knowledge_METWeather.format_weather_now()
    weather_later = knowledge_METWeather.format_weather_later()
    weather_days = knowledge_METWeather.format_future_days()

    # Breakout the data to individual rows
    if weather_now:
        weather_icon_data = weather_types[weather_now['W'][1].strip()]
        weather_temperature_data = weather_now['F']
        weather_rain_probability_data = weather_now['Pp']
        house_temperature_data = "temp/hum data"

    return (weather_icon_data, weather_temperature_data, weather_rain_probability_data, house_temperature_data, weather_later, weather_days, alert_message)


# disable mouse cursor
pygame.mouse.set_visible(0)

# MET Weather
weather_later_count = 4
weather_days_count = 4
weather_later_icons = {}
weather_later_temps = {}
weather_later_timeslots = {}
weather_days_icons = {}
weather_days_temps = {}
weather_days_names = {}
for i in range(0, 4):
    weather_days_icons[i] = text.create_weather_text("", font_weather_icons, 34, WHITE)
    weather_days_temps[i] = text.create_standard_text("", font_standard, 17, WHITE)
    weather_days_names[i] = text.create_standard_text("", font_standard, 16, WHITE)
    weather_later_icons[i] = text.create_weather_text("", font_weather_icons, 34, WHITE)
    weather_later_temps[i] = text.create_standard_text("", font_standard, 17, WHITE)
    weather_later_timeslots[i] = text.create_standard_text("", font_standard, 9, WHITE)

# Add message to show (for a minute) that the application has started
#  and at what time (this will be added to the message queue)
alert_message.add_message("Started at " + gettime.get_time_now(), 1)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Check System Commands
    # TODO - far too chatty, should be placed in a timecycle
    #commands.check_command_and_run()
    
    # clear screen
    screen.fill(BLACK)

    # Time and Date display
    current_time = text.create_standard_text(gettime.get_time_now(), font_standard, 105, WHITE) 
    current_date = text.create_standard_text(gettime.get_date_now(), font_standard, 39, WHITE)

    
    if metWeatherTimecycle.is_alarming():
        # TODO - Now the bloody weather isnt showing on the screen!?!
        knowledge_METWeather.get_weather()
        metWeatherTimecycle.reset_alarm()

    (weather_icon_data, weather_temperature_data, weather_rain_probability_data, house_temperature_data, weather_later, weather_days, alert_message) = get_weather(weather_icon_data, weather_temperature_data, weather_rain_probability_data, house_temperature_data, weather_later, weather_days, alert_message)

    # Set up text placeholders
    weather_icon = text.create_weather_text("", font_weather_icons, 100, WHITE)
    weather_temperature = text.create_standard_text("", font_standard, 40, WHITE)
    weather_rain_probability = text.create_standard_text("", font_standard, 12, WHITE)
    
    if weather_icon_data != "":
        weather_icon = text.create_weather_text(weather_icon_data, font_weather_icons, 100, WHITE)
        weather_temperature = text.create_standard_text(weather_temperature_data[1].replace(" ", "").lower(), font_standard, 40, WHITE)
        weather_rain_probability = text.create_standard_text("rain: %s" % (weather_rain_probability_data[1]), font_standard, 12, WHITE)
        
        if weather_later and weather_later_count and len(weather_later) < weather_later_count:
                weather_later_count = len(weather_later)
        if weather_later:
            count = 0
            while (count < weather_later_count):
                for weather_later_key, weather_later_value in weather_later.items():
                    weather_later_icons[count] = text.create_weather_text("%s" % (weather_later_value['W']), font_weather_icons, 34, WHITE)
                    weather_later_temps[count] = text.create_standard_text("%sc" % (weather_later_value['F']), font_standard, 17, WHITE)
                    weather_later_timeslots[count] = text.create_standard_text("%s" % (weather_later_key), font_standard, 9, WHITE)
                    count += 1
            
        if weather_days and len(weather_days) < weather_days_count:
                weather_days_count = len(weather_days)
        if weather_days:
            count = 0
            while (count < weather_days_count):
                for weather_day_key, weather_day_value in weather_days.items():
                    weather_days_icons[count] = text.create_weather_text("%s" % (weather_day_value['W']), font_weather_icons, 34, WHITE)
                    weather_days_temps[count] = text.create_standard_text("%sc" % (weather_day_value['F']), font_standard, 17, WHITE)
                    weather_days_names[count] = text.create_standard_text("%s" % (weather_day_key), font_standard, 16, WHITE)
                    count += 1

    if weather_later_icons:
        
        # Alert message
        house_temperature = text.create_standard_text(alert_message.get_message(), font_standard, 20, WHITE)
        # System Infomation
        ip = text.create_standard_text(getip.get_ip_address(), font_standard, 12, WHITE)
        screen_size = text.create_standard_text("X:%spx / Y:%spx" % screen.get_size(), font_standard, 12, WHITE)
        screen.blit(current_time, (0, -17))
        screen.blit(current_date, (0, 100))
        screen.blit(weather_icon, (470, 0))
        screen.blit(weather_temperature, (575, 40))
        screen.blit(weather_rain_probability, (580, 85))
        height_step = 110
        weather_left = 460
        for i in range(weather_later_count):
            icon_left = 25 - (get_width(weather_later_icons[i]) / 2)
            screen.blit(weather_later_icons[i], (weather_left + icon_left + i * 50, height_step))
            
            temp_left = 25 - (get_width(weather_later_icons[i]) / 2)
            screen.blit(weather_later_temps[i], (weather_left + temp_left + (i * 50), height_step + 45))
            
            timeslot_left = 25 - (get_width(weather_later_timeslots[i]) / 2)
            screen.blit(weather_later_timeslots[i], (weather_left + timeslot_left + (i * 50), height_step + 80))

        if weather_later_count > 0:
            height_step += 120

        for i in range(weather_days_count):
            icon_left = 25 - (get_width(weather_days_icons[i]) / 2)
            screen.blit(weather_days_icons[i], (weather_left + icon_left + i * 50, height_step))

            temp_left = 25 - (get_width(weather_days_icons[i]) / 2)
            screen.blit(weather_days_temps[i], (weather_left + temp_left + i * 50, height_step + 45))
            
            day_left = 25 - (get_width(weather_days_names[i]) / 2)
            screen.blit(weather_days_names[i], (weather_left + day_left + i * 50, height_step + 80))

        if weather_days_count > 0:
            height_step += 120

        screen.blit(house_temperature, (weather_left + 12, height_step))

        # Would be nice to control the visibility of the sys info from the command module
        screen.blit(screen_size, (0, get_height(screen) - get_height(screen_size) - 20))
        screen.blit(ip, (get_width(screen) - get_width(ip), get_height(screen) - get_height(ip) - 20))

    # sleep now, only dreams (for a second)
    pygame.display.flip()
    time.sleep(2)
