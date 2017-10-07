import Timecycle as timecycle


class Alert:
    # describes the type
    typeDescription = 'Handles and manages alerts'

    def __init__(self):
        self.alert_messages = []
        self.active_message = -1
        self.timecycle = timecycle.Timecycle()
        self.timecycle.wait_time = 1

    def change_message(self):
        if self.alert_messages.count > -1 and self.timecycle.is_alarming():
            if self.active_message < self.alert_messages.count:
                self.active_message += 1
            else:
                self.active_message = 0
        self.timecycle.reset_alarm()
        return self.active_message

    def get_messages(self):
        message = self.change_message()
        if self.active_message > -1 :
            return self.alert_messages[message]
        else:
            return ""
    
alert = Alert()
alert.alert_messages.append("a new message")
alert.active_message = 0
print(alert.get_messages())
alert.active_message = -1
print(alert.get_messages())