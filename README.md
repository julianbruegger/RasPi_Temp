# RasPi_Temp
## Auftrag
Ich sollte für den ICT-BZ Serverraum eine Temperatur/Feuchtigkeits anzeige erstellen. Dies soll in einem Graphen visualisert werden. 

## Vorgehen
### DS18B20
Als erstes habe ich mit einem [DS18B20](./02DS18B20) Sensor gearbeitet. Das auslesen der Daten funktioniert dort über eine Shell-Schnitstelle. 

![Bild eines DS18B20](./data/DS18B20.jpg)

### DHT11
Da aber der Wunsch aufkam auch die Luftfeuchtigkeit aufzuzeigen habe ich von Joe einen DHT11 Sensor ausgeliehen. 
Dieser kann sowohl die Luftfeuchtigkeit als auch die Temperatur messen. 
![Bild eines DS18B20](./data/DHT11.jpg)

Über ein Pythonmodul ``` Adafruit_DHT ``` kann ein solcher sensor ganz eifach ausgelesen werden. 

Über nur 4 Zeilen Code kann der Sensor ganz einfach ausgelesen und geprintet werden.

```python
# Definieren des Sensortyps
sensor = Adafruit_DHT.DHT11
    #Definieren des Verwendetens GPIO-Pin's
    pin = 21
    # Hier definiere ich aus was sich die "humidity" und die "temperature" zusammensetzt. 
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    # Ausgeben der Daten im richtigen Format
    print('{0:03.1f} {1:03.1f}'.format(temperature, humidity))
```
Über ein weiteres Pythonmodul namens ```mysql.connector``` kann wie der Name schon sagt auf eine MySQL Datenbank zugegriffen werden. 

Auch dies Ist ganz simple. Das ganze ist auf der Website von [w3schools.com](https://www.w3schools.com/python/python_mysql_getstarted.asp "Link zu w3shools.com") perfekt dokumentiert.

```python
# Hier definiere ich die Zugangsd
mydb = mysql.connector.connect(
    host="10.20.11.199", 
    user="root",
    password="123ict",
    database="temp_data")
mycursor = mydb.cursor()
#Inser values into db
        sql = "INSERT INTO sensor_1 (time, humidity, temperature) VALUES (now(), %s,%s)"
        val = (humidity, temperature)
        mycursor.execute(sql, val)
        mydb.commit()
```
