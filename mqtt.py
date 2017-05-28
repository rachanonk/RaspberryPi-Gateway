import paho.mqtt.client as mqtt
import time
from sql import StoreTemperature, StoreBrightness

count1 = 0
count2 = 0
temp = 0
temp2 = 0

def publis_temperature():
     mqttc.publish("/ESP/Temperature", "GET", 0)
     time.sleep(1)

def read_temperature():
    mqttc.subscribe("/ESP/Temperature", 0)
    time.sleep(1)

def publis_brightness():
     mqttc.publish("/ESP/Light", "GET", 0)
     time.sleep(1)

def read_brightness():
    mqttc.subscribe("/ESP/Light", 0)
    time.sleep(1)

def read_air():
    mqttc.subscribe("/ESP/AirCon", 0)
    time.sleep(1)

def publish_air(value):
     mqttc.publish("/ESP/Command/AirCon", value, 0)
     time.sleep(1)

def on_message(client, userdata, msg):
	if(msg.payload.decode() == "LON" or msg.payload.decode() == "LOFF"):
		global temp
		temp = msg.payload.decode()   
		print("From Brightness " + msg.payload.decode())
		global count1
		count1 = count1 + 1
		if(count1 == 10):
			StoreBrightness(msg.payload.decode())
			count1 = 0
	if(msg.payload.decode() == "AON" or msg.payload.decode() == "AOFF"):
		global temp2
		temp2  = msg.payload.decode()
	else:
		print("From Temperature " + msg.payload.decode())
		global count2
		count2 = count2 + 1
		if(count2 == 10):
                        StoreTemperature(msg.payload.decode())
                        count2 = 0
	if(temp == "LOFF" and temp2 == "AON"):
		publish_air("OFF")

mqttc = mqtt.Client()
mqttc.on_message = on_message

#Config user
mqttc.username_pw_set("velmpeke", "NdYTjSQFFCdi")
#Connect
mqttc.connect("m11.cloudmqtt.com", 11171, 60)
mqttc.loop_start()

while 1:
    #trick()
    read_temperature()
    read_brightness()
    read_air()

mqttc.loop_stop()
mqttc.disconnect()


