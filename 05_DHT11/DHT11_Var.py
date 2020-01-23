import Adafruit_DHT
import time

while True:
    sensor = Adafruit_DHT.DHT11
    pin = 21
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    print ('{0:0.1f}'.format(temperature))
    print ('{0:0.1f}'.format(humidity))
    #print (Temp)

    time.sleep(10)