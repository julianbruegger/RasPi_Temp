import Adafruit_DHT
import time

while True:
    sensor = Adafruit_DHT.DHT22
    pin = 21
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    time.sleep(10)