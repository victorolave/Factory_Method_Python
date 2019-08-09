from logger import Logger


class ConsoleLogger(Logger):
    def __init__(self, msg):
        print("Console Message:  "+msg)
