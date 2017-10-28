#!/usr/bin/python

import pir_sensor
import transistor_switch
import timecycle

pir_sensor = pir_sensor.pir_sensor()

transistor_switch = transistor_switch.transistor_switch()

time_cycle = timecycle.timecycle()
time_cycle.wait_time = 1
time_cycle.reset_alarm()
time_cycle.force_alarm = True

print(time_cycle.alarm_start)
print(time_cycle.alarm_time)

try:
    while True:
        if time_cycle.is_alarming_manually_reset():
            if pir_sensor.get_reading():
                transistor_switch.switch(True)
                time_cycle.reset_alarm()
            else:
                transistor_switch.switch(False)

except KeyboardInterrupt:
	print("Quit")