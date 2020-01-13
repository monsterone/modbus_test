
import configparser as cparser
import paho.mqtt.client as mqtt
import queue,os
import datetime,time

# ===============读取config.ini文件设置============
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
file_path = base_dir + "/function/tools/config.ini"
cf = cparser.ConfigParser()
cf.read(file_path,encoding='utf-8')

mqtthost = cf.get("MQTT","MQTTHOST")
mqttport = cf.get("MQTT","MQTTPORT")

##连接客户端
MQTTHOST = mqtthost
MQTTPORT = int(mqttport)
mqttClient = mqtt.Client()
q = queue.Queue()

# 连接MQTT服务器
def on_mqtt_connect():
    mqttClient.connect(MQTTHOST, MQTTPORT, 60)
    mqttClient.loop_start()


# publish 消息
def on_publish(topic, payload):
    mqttClient.publish(topic, payload)


# 消息处理函数
def on_message_come(client, userdata, msg):
    # print(msg.topic + " " + ":" + str(msg.payload))
    mss = str(msg.payload)
    # print(msg.topic + " " + ":" + mss)
    q.put(mss)


# subscribe 消息
def on_subscribe(topic):
    mqttClient.subscribe(topic)
    mqttClient.on_message = on_message_come  # 消息到来处理函数
    return mqttClient


#连接mqtt单独
def connect_mqtt():
    on_mqtt_connect()


##第一次连接mqtt
def main1(res,topic, payload):
    on_mqtt_connect()
    on_subscribe(res)
    on_publish(topic,payload)
    return q
    # while True:
    #     pass

##非第一次连接mqtt
def main2(res,topic, payload):
    # on_mqtt_connect()
    on_subscribe(res)
    on_publish(topic,payload)
    ##记录修改时间
    start = time.time()
    return q,start

##发布（性能）
def main3(topic, payload):
    # on_mqtt_connect()
    # on_subscribe(res)
    on_publish(topic,payload)
    return q


if __name__ == '__main__':
    main1()

