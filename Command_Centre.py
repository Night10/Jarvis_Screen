from urllib2 import urlopen
from urllib import urlencode
import platform


class Command_Centre:
    # describes the type
    typeDescription = 'Runs a command if one is present within a text file'

    # Setting an immutable default value
    # http://stackoverflow.com/questions/2681243/how-should-i-declare-default-values-for-instance-variables-in-python
    
    # define default command file path
    #default_command_path = 'http://127.0.0.1/command.txt'
    #default_command_url = 'http://127.0.0.1/command.php'
    
    default_command_path = 'http://boncester.serveftp.com/projects/jarvis/command.txt'
    default_command_url = 'http://boncester.serveftp.com/projects/jarvis/command.php'

    def __init__(self, command_file_path = default_command_path, command_file_post = default_command_url):
        self.command_file_path = command_file_path
        self.command_file_post = command_file_post
        self.commands_found = []
        self.command_search = ['reset', 'shutdown', 'refreshweather']

    def load_command_file(self):
        data = urlopen(self.command_file_path).read(20000)
        commands = data.split(',')
        return commands
    
    def clear_command_file(self):
        url = self.command_file_post
        data = urlencode({'dave' : 'stewart'})
        content = urlopen(url=url, data=data).read()

    def check_command_and_run(self):
        self.commands = self.load_command_file()
        for search_command in self.command_search:
            # If a command has been received
            if search_command in self.commands:
                # Clear the command file contents
                self.clear_command_file()

                # Run the underlying command
                if search_command == 'shutdown':
                    self.shutdown()
                if search_command == 'reset':
                    self.restart()
                if search_command == 'refreshweather':
                    self.refresh_weather()
        return self.commands

    def restart(self):
        if platform.system() == 'Linux':
            command = "/usr/bin/sudo /sbin/shutdown -r now"
            import subprocess
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output = process.communicate()[0]
            print output

    def shutdown(self):
        if platform.system() == 'Linux':
            command = "/usr/bin/sudo /sbin/shutdown"
            import subprocess
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output = process.communicate()[0]
            print output