# encoding: utf-8
import mp
import paho.mqtt.client as mqtt



def on_connect(client, userdata, flags, rc):
    print("Connected with result code MONSTER " + str(rc))
    client.subscribe("response/456/22fcb880-2ba4-11ea-9856-6362f387f47c@18")


def on_message(client, userdata, msg):
    mss = str(msg.payload)
    print(msg.topic + " " + ":" + mss)
    mp.put(mss)


def connect():
   client = mqtt.Client()
   client.on_connect = on_connect
   client.on_message = on_message
   client.connect("192.168.1.192", 1883, 60)
   client.loop_forever()



def subscriber(client):
    client.on_connect = on_connect
    client.on_message = on_message
    # client.connect("192.168.1.192", 1883, 60)
    client.loop_forever()



# connect()