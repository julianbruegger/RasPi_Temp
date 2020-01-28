import Adafruit_DHT
import time
import mysql.connector


# Define db
mydb = mysql.connector.connect(
    host="10.20.11.113", 
    user="root",
    password="123ict",
    database="temp_data")
mycursor = mydb.cursor()

sensor = Adafruit_DHT.DHT11
pin = 21

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    sql = "INSERT INTO sensor_1 (time, humidity, temperature) VALUES (now(), %s,%s)"
    val = (humidity, temperature)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

    time.sleep(10)
    