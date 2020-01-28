import time
 
sensor = '/sys/bus/w1/devices/28-02161f5a48ee/w1_slave'
 
def readTempSensor(sensorName) :
    """Aus dem Systembus lese ich die Temperatur der DS18B20 aus."""
    f = open(sensorName, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
while True :
    """Mit einem Timestamp versehe ich meine Messung und lasse mir diese in der Console ausgeben."""
    print(time.strftime('%H:%M:%S') +" - " + str(readTempSensor(sensor)))
    # Nach 10 Sekunden erfolgt die nächste Messung
    time.sleep(10)