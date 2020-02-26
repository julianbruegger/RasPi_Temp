import Adafruit_DHT
import time
import mysql.connector
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

maxtemp = 28.0
message = '!ALARM! Temperatur liegt bei '
message2 = ' Bitte Klimageraet kontrollieren'

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

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = '#'
auth_token = '#'
client = Client(account_sid, auth_token)

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
        send = (message + str(temperature) + message2)
        if temperature > maxtemp:
            print("Temp is to High, Checking again")
            time.sleep(60)
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)           
            if temperature > maxtemp:
                print (send)
                message = client.messages \
                    .create(
                        body=(send),
                        from_='+12037936858',
                        to='+41765974891'
                    )
                time.sleep(60)
            else:
                print("False Alarm")
        else:
            print("Everything is fine")
            time.sleep(60)
    
