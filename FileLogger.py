import os
from logger import Logger


class FileLogger(Logger):
    def __init__(self, msg):

        file = open("C:/Users/vicol/Desktop/message.txt", "w")
        file.write(msg)
        file.close()

        print("Message: " + msg + ", is saved.")
