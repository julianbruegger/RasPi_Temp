# !/bin/bash

while :
    do
    # Temperatur auslesen
    tempread=`cat /sys/bus/w1/devices/28-0316a2797668/w1_slave`
    # Format
    temp=`echo "scale=2; "\`echo ${tempread##*=}\`" / 1000" | bc`
    
    # Output
    {
        echo "<!DOCTYPE html>"    
        echo "<html lang="de">"
        echo "<head>"
        echo "<link rel="stylesheet" type="text/css" href="style.css" media="screen" />"
        echo "<meta charset="utf-8">"
        echo "<title> Mein Temperatur-Sensor </title>"
        echo "</head>"
        echo "<body>"
        echo "<img src="https://www.ict-bz.ch/themes/ict-bz/assets/logo.svg">"
        echo "<h1> Temperatur im Serverraum"
        echo "</h1>"
        echo "<p> The measured temperature is " $temp "°C" 
        echo "</p>"
        echo "</body>"
        echo "</html>"

        
    }> /var/www/html/index.html
sleep 5
done