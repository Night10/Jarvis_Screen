from datetime import datetime
from datetime import timedelta


class alert_message:
    """ For managing alerts """
    typeDescription = 'Handles and manages alerts'

    def __init__(self):
        self.alert_messages = []
        self.active_message = -1
        self.message_timeout = 5  # minutes

    def change_message(self):
        """ Sets the active message """
        self.remove_messages()
        alert_messages_length = len(self.alert_messages)
        if alert_messages_length > 0:
            if self.active_message < alert_messages_length - 1:
                self.active_message = self.active_message + 1
            else:
                self.active_message = 0

        return self.active_message

    def remove_messages(self):
        """ Removes messages that have expired """
        if len(self.alert_messages) > -1:
            cleared_messages = []
            now_in_seconds = datetime.now().strftime("%s")
            for message in self.alert_messages:
                if message[0]['timeout'].strftime("%s") >= now_in_seconds:
                    cleared_messages.append(message)
            del self.alert_messages[:]
            self.alert_messages = cleared_messages

    def add_message(self, message, timeout):
        """ Adds  a message to the collection """
        if timeout is None:
            timeout = datetime.now() + timedelta(minutes=self.message_timeout)
        else:
            timeout = datetime.now() + timedelta(minutes=timeout)
        if message is None:
            return False
        
        self.alert_messages.append([{'message': message, 'timeout': timeout}])

        return True

    def get_message(self):
        """ Gets the message to be returned """
        self.change_message()
        if self.active_message > -1:
            return self.alert_messages[self.active_message]
        else:
            return None

# TODO - CGMORSE - Testing only, remove when implementation complete
alert = alert()
alert.add_message('dave stewart', 5)
alert.add_message('is a hacker', 12)
message = alert.get_message()
print(message[0]['message'])
message = alert.get_message()
print(message[0]['message'])
message = alert.get_message()
print(message[0]['message'])