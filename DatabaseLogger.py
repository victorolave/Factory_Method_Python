from logger import Logger


class DatabaseLogger(Logger):
    def __init__(self, msg):
        print("Database Message:  " + msg)