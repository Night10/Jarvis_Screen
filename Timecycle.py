#imports
from datetime import datetime
import time


class Timecycle:
    # describes the type
    typeDescription = 'Creates a timeable instance we can use for timing cycles of things'

        # Setting an immutable default value
    # http://stackoverflow.com/questions/2681243/how-should-i-declare-default-values-for-instance-variables-in-python

    def __init__(self, wait_in_minutes=15):
        self.wait_in_minutes = wait_in_minutes
        self.minutes_remaining = self.wait_in_minutes
        self.time_format = '%H:%M:%S'
        self.start_timing = datetime.now()

    def time_check(self):
        temp_minutes_remaining = self.get_minutes_difference(self.start_timing, datetime.now())
        if temp_minutes_remaining <= 0:
            self.minutes_remaining = 0
        else:
            self.minutes_remaining = self.minutes_remaining - temp_minutes_remaining

        if self.minutes_remaining == 0:
            # Reset minutes_remaining counter and start_timing datetime.now
            self.minutes_remaining = 15
            self.start_timing = datetime.now()
            return True
        else:
            return False

    def get_minutes_difference(self,starts, now):
        # Taken from SO: http://stackoverflow.com/questions/2788871/python-date-difference-in-minutes
        d1_ts = time.mktime(starts.timetuple())
        d2_ts = time.mktime(now.timetuple())

        return int(d2_ts-d1_ts) / 60
