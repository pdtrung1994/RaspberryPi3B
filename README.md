<meta http-equiv="refresh" content="0; url=./index.html" />

# RaspberryPi3B
*(This README is visible only on GitHub, not on GitHub Pages)*

[Click here if not redirected](index.html)


GUIDE & Summary Support

pip install google-api-python-client

pip install RPi.GPIO

MCP3008.py : Read voltage from MCP3008 pin

mq2.py : Convert voltage to ppm for MQ2 sensor

send_data_gg.py : send data to google drive

read_mq_voltage.py : send all pin data with MQ2, MQ3, MQ5, MQ7, MQ8, MQ135

.json file : Get from google cloud API : https://developers.google.com/workspace/guides/create-credentials > go to service account > create project (if no project)

NOTE : 
```
need to add permission

need 'sudo apt-get install ntp' to config datetime for google api

run at starup - @reboot cd /home/pi/FTP/code/ && python3 read_mq_voltage.py
```
NOTE 2:
```
On a new Rashberry Pi
- Connect SD card to PC -> install rashberry PI OS: https://www.raspberrypi.com/software/ (can setting user & wifi)
- Connect SD card back to rashberry PI -> connect RPI to monitor -> should working
- Install Python:
- $ sudo apt-get update
- $ sudo apt-get install python3

connect SSH: https://raspberrypi-guide.github.io/networking/connecting-via-ssh
find RPI ip -> run terminal on RPI -> ifconfig
enable SSH -> run terminal on RPI -> sudo raspi-config -> enable SSH
with pc terminal => ssh <user>@<ip-here>

if you want to send file to RPI
download PuTTY -> redirect to PuTTy folder to use pscp
-> pscp.exe -P 22 -pw <password-here> "<pc-file-path>" <user>@<RPI-ip-here>:<RPI-file-path>
* example : pscp.exe -P 22 -pw azure "D:\python\code\data_collection.py" azure@192.168.0.43:/home/azure/code/example.py
```
