import timecycle as timecycle
from datetime import datetime
from datetime import timedelta


class Alert:
    # describes the type
    typeDescription = 'Handles and manages alerts'

    def __init__(self):
        self.alert_messages = []
        self.default_timeout = 5  # minutes
        self.active_message = -1
        self.timecycle = timecycle.timecycle()
        self.timecycle.wait_time = 1

    # TODO - CGMORSE - Messages should have a default timout
    #                - that removes them from the collection (using Timecycle)

    # TODO - CGMORSE - The caller should be able to override
    #                -  the default timout of a given message

    def change_message(self):
        # TODO - CGMORSE - this needs to account for current message timout
        if self.alert_messages.count > -1 and self.timecycle.is_alarming():
            if self.active_message < self.alert_messages.count:
                self.active_message += 1
            else:
                self.active_message = 0
        self.timecycle.reset_alarm()
        return self.active_message

    def add_message(self, message, timeout):
        if timeout is None:
            timeout = self.default_timout
        
        if message is None:
            return False
        
        self.alert_messages.append({'message' : message, 'timeout' : timout})
        return True

    def get_messages(self):
        message = self.change_message()
        if self.active_message > -1:
            return self.alert_messages[message]
        else:
            return ""