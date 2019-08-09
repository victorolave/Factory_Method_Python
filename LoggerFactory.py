from FileLogger import FileLogger
from ConsoleLogger import ConsoleLogger
from DatabaseLogger import DatabaseLogger

class LoggerFactory(object):
    def get_log(self, msg, type):

        if type is 'Console':
            return ConsoleLogger(msg)

        elif type is 'File':
            return FileLogger(msg)

        elif type is 'Database':
            return DatabaseLogger(msg)