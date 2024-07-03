pip install google-api-python-client

pip install RPi.GPIO

MCP3008.py : Read voltage from MCP3008 pin

mq2.py : Convert voltage to ppm for MQ2 sensor

send_data_gg.py : send data to google drive

read_mq_voltage.py : send all pin data with MQ2, MQ3, MQ5, MQ7, MQ8, MQ135

.json file : Get from google cloud API : https://developers.google.com/workspace/guides/create-credentials > go to service account > create project (if no project)

NOTE : 

need to add permission

need 'sudo apt-get install ntp' to config datetime for google api


