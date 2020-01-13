

import sys
import os
import unittest
import configparser as cparser
from time import sleep
from ddt import ddt, data, unpack
from function.asever import keep
from mqtt.pub_sub import connect_mqtt
# sys.path.append("F:\\Project\\New\\modbus_test\\mqtt")


# ===============读取config.ini文件设置============


base_dir = str(os.path.dirname(os.path.dirname(__file__)))
file_path = base_dir + "/tools/config.ini"
cf = cparser.ConfigParser()
cf.read(file_path, encoding='utf-8')
TOTIL = cf.get("DEVICE", "TOTIL")

# 总子设备数
total = int(TOTIL)

# a2 = list(range(1, 98, 4))
#
# @ddt
class Fun(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # back = keep(2, first=True)
        # back1 = back.get()
        # # self.assertIn('555',back1)
        # print(back1 + "连接")
        ##连接mqtt
        connect_mqtt()
        print("连接mqtt")

    @classmethod
    def tearDownClass(cls):
        pass

    # 01线圈
    def test6_read_coil(self):
        '''读-线圈'''
        for id in range(0, total - 3, 4):
            back = keep(id)
            back1 = back.get()
            self.assertIn('1', back1)
            print(back1)

    def test5_write_coil(self):
        '''写-线圈'''
        for id in range(0, total - 3, 4):
            back = keep(id, 'write')
            back1 = back.get()
            self.assertIn('true', back1)
            print(back1)

    # 02离散输入
    def test4_ls_input(self):
        '''读-离散输入'''
        for id in range(1, total-2, 4):
            back = keep(id)
            back1 = back.get()
            self.assertIn('0', back1)
            print(back1)

    # @data(*a2)
    # def test4_ls_input1(self, id):
    #     '''读-离散输入'''
    #     print(id)
    #     back = keep(id)
    #     back1 = back.get()
    #     self.assertIn('0', back1)
    #     print(back1)

    # 04输入寄存器
    def test3_input_jc(self):
        '''读-输入寄存器'''
        for id in range(3, total, 4):
            back = keep(id)
            back1 = back.get()
            self.assertIn('0', back1)
            print(back1)

    # 03保持集成器
    def test2_read_hold(self):
        '''读-保持寄存器'''
        for id in range(2, total - 1, 4):
            back = keep(id)
            back1 = back.get()
            self.assertIn('555', back1)
            print(back1)

    def test1_write_hold(self):
        '''写-保持寄存器'''
        for id in range(2, total - 1, 4):
            back = keep(id, 'write')
            back1 = back.get()
            self.assertIn('true', back1)
            print(back1)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(Fun("test1_write_hold"))
    # suite.addTest(Fun("test2_read_hold"))
    # suite.addTest(Fun("test3_input_jc"))
    # suite.addTest(Fun("test4_ls_input"))
    # suite.addTest(Fun("test5_write_coil"))
    suite.addTest(Fun("test6_read_coil"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

    # unittest.main()
