import paho.mqtt.client as mqtt
import time

def trick():
    mqttc.publish("/ESP/Temperature", "GET", 0)
    time.sleep(1)

def read():
    mqttc.subscribe("/ESP/Temperature", 1)
    time.sleep(1)

mqttc = mqtt.Client()
mqttc.connect("m11.cloudmqtt.com", 11171, 60)
mqttc.loop_start()

while 1:
    trick()
    read()

mqttc.loop_stop()
mqttc.disconnect()

