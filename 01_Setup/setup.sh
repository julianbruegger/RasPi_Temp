sudo apt-get update
sudo apt-get upgrade
sleep 1

echo "Updates Heruntergeladen und Installiert!"
echo ""
echo ""
echo "DHT11 Zusatzpakete Installieren"

sudo apt-get install build-essential python-dev python-openssl git
git clone https://github.com/adafruit/Adafruit_Python_DHT.git && cd Adafruit_Python_DHT
sudo python setup.py install

echo "Alles wichtige ist nun Installiert"