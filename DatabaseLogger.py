import mysql.connector
from logger import Logger

dbConnect = {
    'host':'localhost',
    'user':'root',
    'password':'victor1131',
    'database':'messages'
}

conexion = mysql.connector.connect(**dbConnect)

class DatabaseLogger(Logger):
    def __init__(self, msg):
        cursor = conexion.cursor()
        sql = "INSERT INTO messages (id, message) VALUES (%s,%s)"
        cursor.execute(sql, (None, msg))
        conexion.commit()

        print("Message: " + msg + ", saved in database")
        print("Database Message:  " + msg)