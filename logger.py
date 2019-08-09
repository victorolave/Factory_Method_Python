class Logger(object):

    def __init__(self):
        self.message = None

    def log(self, msg):
        self.message = msg
        return self.message

    def __str__(self):
        return self.message

