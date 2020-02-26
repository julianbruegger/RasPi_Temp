import Adafruit_DHT
import time

while True:
    sensor = Adafruit_DHT.DHT22
    pin = 21
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print('{0:03.1f} {1:03.1f}'.format(temperature, humidity))
    
    time.sleep(10)