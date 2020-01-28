#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import sys
import mysql.connector
 
sensor = '/sys/bus/w1/devices/28-0316a2794a82/w1_slave'

# Define db
mydb = mysql.connector.connect(
    host="10.20.11.199", 
    user="root",
    password="123ict",
    database="temp_data")
mycursor = mydb.cursor()

def readTempSensor(sensorName) :
    """Aus dem Systembus lese ich die Temperatur der DS18B20 aus."""
    f = open(sensorName, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def readTempLines(sensorName) :
    lines = readTempSensor(sensorName)
    temperaturStr = lines[1].find('t=')
    # Ich überprüfe ob die Temperatur gefunden wurde.
    if  temperaturStr != -1 :
        tempData = lines[1][temperaturStr+2:]
        tempCelsius = float(tempData) / 1000.0
        tempKelvin = 273 + float(tempData) / 1000
        tempFahrenheit = float(tempData) / 1000 * 9.0 / 5.0 + 32.0
    return [tempCelsius, tempKelvin, tempFahrenheit]

print(str(readTempLines(sensor)[0]))
while True :
    temperature=(str(readTempLines(sensor)[0]))
    sql = "INSERT INTO sensor_2 (time, temperature) VALUES (now(), 'temperature')"
    val = (temperature)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

    time.sleep(10)