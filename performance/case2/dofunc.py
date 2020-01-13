import datetime
import random
import sys
import os
import time
import unittest
import configparser as cparser
from time import sleep
from ddt import ddt, data, unpack
from function.asever import keep
from function.tools.timeformat import timefor
from mqtt.pub_sub import connect_mqtt


# ===============读取config.ini文件设置============
base_dir = str(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
file_path = base_dir + "/function/tools/config.ini"
cf = cparser.ConfigParser()
cf.read(file_path, encoding='utf-8')
TOTIL = cf.get("DEVICE", "TOTIL")
# 总子设备数
total = int(TOTIL)


'''modbus读写操作类'''

class FunBus():

    #####=============== 01线圈
    def test6_read_coil(self):
        '''读-线圈'''
        ##连接mqtt
        # connect_mqtt()
        id = random.randrange(0, total - 3, 4)
        back = keep(id)
        back1 = back.get()
        time1 = timefor()
        print(time1, end=' ')
        print("读-线圈:",back1)

    def test5_write_coil(self):
        '''写-线圈'''
        ##连接mqtt
        # connect_mqtt()
        id = random.randrange(0, total - 3, 4)
        back = keep(id, 'write')
        back1 = back.get()
        time1 = timefor()
        print(time1, end=' ')
        print("写-线圈:",back1)

    #####===============02离散输入
    def test4_ls_input(self):
        '''读-离散输入'''
        ##连接mqtt
        # connect_mqtt()
        id = random.randrange(1, total-2, 4)
        back = keep(id)
        back1 = back.get()
        time1 = timefor()
        print(time1, end=' ')
        # self.assertIn('0', back1)
        print("读-离散输入:",back1)

    #####===============04输入寄存器
    def test3_input_jc(self):
        '''读-输入寄存器'''
        ##连接mqtt
        # connect_mqtt()
        id = random.randrange(3, total, 4)
        back = keep(id)
        back1 = back.get()
        time1  = timefor()
        print(time1,end=' ')
        print("读-输入寄存器:",back1)

    #####===============03保持集成器
    def test2_read_hold(self):
        '''读-保持寄存器'''
        ##连接mqtt
        # connect_mqtt()
        id = random.randrange(2, total - 1, 4)
        back = keep(id)
        back1 = back.get()
        time1 = timefor()
        print(time1, end=' ')
        print("读-保持寄存器:",back1)

    def test1_write_hold(self):
        '''写-保持寄存器'''
        ##连接mqtt
        # connect_mqtt()
        id = random.randrange(2, total - 1, 4)
        back = keep(id, 'write')
        back1 = back.get()
        time1 = timefor()
        print(time1, end=' ')
        # self.assertIn('true', back1)
        print("写-保持寄存器:",back1)


if __name__ == '__main__':
    # FunBus().test2_read_hold()
    FunBus().test4_ls_input()
