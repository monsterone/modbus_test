# encoding: utf-8
from time import sleep

import paho.mqtt.client as mqtt

class Pub():

    def __init__(self):
        self.HOST = "192.168.1.192"
        self.PORT = 1883


    def test_write(self,id):
        id1 = id
        id = str(id)
        client = mqtt.Client()
        client.connect(self.HOST, self.PORT, 60)
        client.publish('command/456/22fcb880-2ba4-11ea-9856-6362f387f47c@'+id, '{"id":13,"action":"writeProperty","data":["value",222]}')  # 发布一个主题为'chat',内容为‘hello liefyuan’的信息
        client.loop_forever()



    def test_read(self,id,client):
        id = 18
        id = str(id)
        # client = mqtt.Client()
        # client.connect(self.HOST, self.PORT, 60)
        client.publish('command/456/22fcb880-2ba4-11ea-9856-6362f387f47c@'+id, '{"id":13,"action":"readProperty","data":["value"]}')  # 发布一个主题为'chat',内容为‘hello liefyuan’的信息
        client.loop_forever()






if __name__ == '__main__':
    # Pub().test_write(18)

    Pub().test_read(18)


