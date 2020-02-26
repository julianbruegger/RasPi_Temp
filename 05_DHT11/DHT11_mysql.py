import Adafruit_DHT
import time
import mysql.connector

null_variable = None
# Define db
mydb = mysql.connector.connect(
    host="10.20.11.199", 
    user="root",
    password="123ict",
    database="temp_data")
mycursor = mydb.cursor()

sensor = Adafruit_DHT.DHT22
pin = 21

while True:
    # Get temperature
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is null_variable:
        print('Value is null')
        time.sleep(60)
    
    else:
        #Inser values into db
        sql = "INSERT INTO sensor_1 (time, humidity, temperature) VALUES (now(), %s,%s)"
        val = (humidity, temperature)
        mycursor.execute(sql, val)
        mydb.commit()
        time.sleep(60)
