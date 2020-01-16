# Auslesen der Temperatur

Über das File ´export_html.sh´ wird der aktuelle Sensorwert exportiert. 

Zuerst eröffnen wir eine While schlaufe (Undendlicher loop).

Danach wird die Temperatur ausgelesen.
```sh 
    while :
    do
    # Temperatur auslesen
    tempread=`cat /sys/bus/w1/devices/28-0316a2797668/w1_slave`
```
Danach wird dieser Wert exportiert und durch Tausend geteilt da dieser in einem 5-stelligen Wert eyportiert wird. 
``` sh
    # Format
    temp=`echo "scale=2; "\`echo ${tempread##*=}\`" / 1000" | bc`
```    
Nun wird der Output als `echo` in ein HTML file exportiert. Dies ist wie folgt aufgebaut. 
```sh
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
```
