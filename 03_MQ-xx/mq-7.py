import RPi.GPIO as GPIO
import time
import mysql.connector

null_variable = None
# Define db
mydb = mysql.connector.connect(
    host="10.20.10.199", 
    user="sensor",
    password="***",
    database="Sensor_Data")
mycursor = mydb.cursor()
# change these as desired - they're the pins connected from the
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8
mq7_dpin = 26
mq7_apin = 0

#init defiinieren

def init():
    GPIO.setwarnings(False)
    GPIO.cleanup() #Macht die GPIO-Pins frei
    GPIO.setmode(GPIO.BCM) #Die Nummerierungsart der GPIO definieren

    # set up the SPI interface pins
    GPIO.setup(SPIMOSI, GPIO.OUT)
    GPIO.setup(SPIMISO, GPIO.IN)
    GPIO.setup(SPICLK, GPIO.OUT)
    GPIO.setup(SPICS, GPIO.OUT)
    #Wiederstand anpassen
    GPIO.setup(mq7_dpin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

# Nun die daten aus dem MPC3008 auslesen

def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)	

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout

#main ioop
def main():
        init()
        print"please wait..."
        time.sleep(20)
        while True:
                co_val = str((COlevel/1024.)*25)
                COlevel=readadc(mq7_apin, SPICLK, SPIMOSI, SPIMISO, SPICS)
                #print("CO is detected")
                print"Current CO AD vaule = " +str("%.2f"%((COlevel/1024.)*25))+" ppm"
                print"Current CO density is:" +str((COlevel/1024.)*25)+" %"
                sql = "INSERT INTO sensor_3 (time, co, co_2) VALUES (now(), %s,%s)"
                val = (co_val, co_val)
                mycursor.execute(sql, val)
                mydb.commit()
                time.sleep(0.5)


if __name__ =='__main__':
        try:
                main()
                pass
        except KeyboardInterrupt:
                pass

GPIO.cleanup()

