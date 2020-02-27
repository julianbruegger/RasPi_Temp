import Adafruit_DHT
import time
import mysql.connector
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

maxtemp = 28.0
message = 'Die Temperatur im Serverraum liegt bei '
message2 = 'C und ist somit ueber dem definierten hoechtstwert von '
message3 = 'C.'
message4 = 'Klimageraet kontrollieren!'

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
account_sid = '*'
auth_token = '*'
client = Client(account_sid, auth_token)

while True:
    # Get temperature
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    # Check if vallue is null
    if humidity is null_variable:
        print('Value is null')
        time.sleep(60)
    else:
  
        #Inser values into db
        sql = "INSERT INTO sensor_1 (time, humidity, temperature) VALUES (now(), %s,%s)"
        val = (humidity, temperature)
        mycursor.execute(sql, val)

        mydb.commit()
        temp_Format = ('{0:03.1f}'.format(temperature))
        # print('{0:03.1f} {1:03.1f}'.format(temperature, humidity))
        send = ((message)+(str(temp_Format))+(message2)+(str(maxtemp))+(message3)+(message4))
        # Check if Temp is to high
        if temperature > maxtemp:
            # If True check after one minute again
            print("Temp is to High, Checking again")
            time.sleep(60)
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)           
            if temperature > maxtemp:
                print (send)
                #If still to high send SMS to Number
                message = client.messages \
                    .create(
                        body=(send),
                        from_='+12037936858',
                        to='+*'
                    )
                time.sleep(600)
            # If second Test is false, abort
            else:
                #print("False Alarm")
                time.sleep(10)
        # If first test is false, abort.
        else:
            #print("Everything is fine")
            time.sleep(300)
    
