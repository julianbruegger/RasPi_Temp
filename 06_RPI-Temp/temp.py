from gpiozero import CPUTemperature
import time
import mysql.connector

while True:
    cpu = CPUTemperature()
    temp=str(cpu.temperature)

    # DB definieren
    null_variable = None
    # Define db
    mydb = mysql.connector.connect(
        host="192.168.111.214", 
        user="Sensor",
        password="+++",
        database="Sensor_Data")
    mycursor = mydb.cursor()

    sql = "INSERT INTO sensor_4 (time, temp) VALUES (now()," + temp + ")"
    mycursor.execute(sql)
    mydb.commit()
    time.sleep(30)