from datetime import datetime
from datetime import timedelta
import time


class Timecycle:
    # describes the type
    typeDescription = 'Creates a timeable instance we can use for timing cycles of things'

    def __init__(self):
        self.wait_time = 15
        self.alarm_start = datetime.now()
        self.wait_time = timedelta(minutes=self.wait_time)
        self.alarm_time = self.alarm_start + self.wait_time
        self.force_alarm = False

    def reset_alarm(self):
        self.alarm_start = datetime.now()

    def is_alarming(self):
        now = datetime.now().strftime("%s")
        alarm_time = self.alarm_time.strftime("%s")
        if now > alarm_time or self.force_alarm:
            self.reset_alarm()
            return True
        else:
            return False
