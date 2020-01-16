# Grundlegende einrichtungen des Raspberry

Über das File `ssh` wird automatisch ssh auf dem Raspberry-Pi aktiviert. 
Dieses File hat keinen inhalt und wird in das Boot verzeichnis der SD-Karte gezogen.

Zusätzlich wird das File `wpa_supplican.conf` erstellt.

Dieses File hat folgenden Inhalt:
``` conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=DE

network={
   ssid="wlan_ssid_eintragen"
   scan_ssid=1
   psk="wlan_passwort_eintragen"
}
}
```

Durch dieses verbindet der Raspberry-Pi sich automatisch mit dem darin angegebenen WLAN.


Weiter kann das Script `setup.sh` ausgefügrt werden. 