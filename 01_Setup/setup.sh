#!/bin/bash

echo "Updates Installieren"
sudo apt-get update
sudo apt-get upgrade


echo "Updates Heruntergeladen und Installiert!"
echo ""
echo ""
echo "DHT11 Zusatzpakete Installieren"

sudo apt-get install build-essential python-dev python-openssl git
git clone https://github.com/adafruit/Adafruit_Python_DHT.git && cd Adafruit_Python_DHT
sudo python setup.py install
echo "MySQL-connector Installieren"
python -m pip install mysql-connector
python -m pip install mysql-connector-python

echo "Alles wichtige ist nun Installiert"
clear

echo "Weitere Informationen im README.md"