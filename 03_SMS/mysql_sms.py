import mysql.connector
from twilio.rest import Client

#Max-Temp for Alert
maxtemp = '25.00'

# Define db
mydb = mysql.connector.connect(
    host="10.20.11.199", 
    user="root",
    password="123ict",
    database="temp_data")

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC4cdfe2590338975f851894a2b21052fa'
auth_token = '3a6154a2c5032d69808cb945479364a2'
client = Client(account_sid, auth_token)

mycursor = mydb.cursor()

mycursor = mydb.cursor()

mycursor.execute("SELECT temperature FROM sensor_1")

myresult = mycursor.fetchone()

def Printdata(myresult):
    return myresult[11:15]

#print(maxtemp)
print(myresult)

#if myresult > maxtemp
    #message = client.messages \
     #   .create(
      #      body=(myresult),
       #     from_='+12037936858',
        #    to='+41765974891'
        #)
#else 
#print("Temperatur ist unter"(maxtemp) Grad)

#print(message.sid)
#print(myresult)
