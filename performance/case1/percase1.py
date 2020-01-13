import random
import sys
import json
import os,time,datetime
import unittest
import configparser as cparser
from time import sleep
from ddt import ddt, data, unpack
from function.asever import keep, keep2
from modbus.modbus_add import ModbusClient


# ===============读取config.ini文件设置============
from mqtt.pub_sub import connect_mqtt
from performance.case1 import testcount

'''配置文件加载'''
base_dir = str(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
file_path = base_dir + "/function/tools/config.ini"
cf = cparser.ConfigParser()
cf.read(file_path, encoding='utf-8')
TOTIL = cf.get("DEVICE", "TOTIL")

# 总子设备数
total = int(TOTIL)

# a2 = list(range(1, 98, 4))
# @ddt
class Fun():

    ##=========数据修改刷新==========
    '''01线圈'''
    def test6_read_coil(self):
        '''读-线圈'''
        ##连接mqtt
        connect_mqtt()
        print("连接mqtt")
        ##初始化modbus数据
        for id in range(0, total - 3, 4):
            ModbusClient().WRITE_SINGLE_COIL(id, 1, 0)
        time.sleep(3)
        nums = []
        for id in range(0, total - 3, 4):
            ##修改modbus线圈数据
            ModbusClient().WRITE_SINGLE_COIL(id,1,1)
            ##记录修改时间
            start = datetime.datetime.now()
            startTime = time.time()
            ##mqtt读取数据
            back,start0 = keep(id)
            ##得到返回值
            back1 = eval(back.get())
            value = json.loads(back1)
            ##判断是否为修改数据
            if value['result'] != 1:
                ##循环订阅，直到读到修改数据
                while True:
                    back2 = keep2(id)
                    back2 = eval(back2.get())
                    # print(back2)
                    value2 = json.loads(back2)
                    if value2['result'] == 1:
                        ##结束时间
                        # end = datetime.datetime.now()
                        endTime = time.time()
                        break
            elif value['result'] == 1:
                # end = datetime.datetime.now()
                endTime = time.time()
            #计算时间差
            duration = endTime - startTime
            print("延时(秒):",duration)
            #时间差统计
            nums.append(duration)
        #调用统计函数
        num, means,medians,var = testcount.getcount(nums)
        print("总数：{}，平均值:{:.2f},中位数:{:.2f},方差：{}".format(num, means, medians, var))


    '''03保持集成器'''
    def test2_read_hold(self):
        '''读-保持寄存器'''
        ##连接mqtt
        connect_mqtt()
        print("连接mqtt")
        ##初始化modbus保持寄存器数据
        for id in range(2, total - 1, 4):
            ModbusClient().WRITE_SINGLE_REGISTER(id, 1, 0)
            # print("lllll")
        time.sleep(3)
        nums = []
        for id in range(2, total - 1, 4):
            ##产生一个随机函数
            beg = random.randint(1, 32677)
            ##修改modbus保持寄存器数据
            ModbusClient().WRITE_SINGLE_REGISTER(id, 1, beg)
            ##记录修改时间
            start = time.time()
            ##mqtt读取数据
            back,start0 = keep(id)
            ##得到返回值
            back1 = eval(back.get())
            value = json.loads(back1)
            if value['result'] != beg:
                while True:
                    back2 = keep2(id)
                    back2 = eval(back2.get())
                    # print(back2)
                    value2 = json.loads(back2)
                    if value2['result'] == beg:
                        ##结束时间
                        end = time.time()
                        break
            elif value['result'] == beg:
                end = time.time()
            # 时间差(秒)
            times = end - start
            #输出时间差
            print("延时(秒):",times)
            # 时间差统计
            nums.append(times)
            # print(nums)
            # 调用统计函数
        num, means, medians, var = testcount.getcount(nums)
        print("总数：{},平均值:{:.2f},中位数:{:.2f},方差：{}".format(num, means, medians, var))




    ##=========数据读取延时==========
    # 02离散输入
    def test4_ls_input(self):
        '''读-离散输入'''
        ##连接mqtt
        connect_mqtt()
        print("连接mqtt")
        nums = []
        for id in range(1, total - 2, 4):
            back,start = keep(id)
            back1 = eval(back.get())
            value = json.loads(back1)
            if value['result'] == 0:
                ##结束时间
                end = time.time()
            # 时间差(毫秒)
            times = (end - start)*1000
                # 输出时间差
            print("延时(毫秒)：",times)
            # 时间差统计
            nums.append(times)
            # print(nums)
            # 调用统计函数
        num, means, medians, var = testcount.getcount(nums)
        print("总数：{},平均值:{:.2f},中位数:{:.2f},方差：{}".format(num, means, medians, var))

    # 04输入寄存器
    def test3_input_jc(self):
        '''读-输入寄存器'''
        ##连接mqtt
        connect_mqtt()
        print("连接mqtt")
        nums = []
        for id in range(3, total, 4):
            back,start = keep(id)
            back1 = eval(back.get())
            value = json.loads(back1)
            if value['result'] == 0:
                #结束时间
                end = time.time()
            # 时间差(毫秒)
            times = (end - start)*1000
            # 输出时间差
            print("延时(毫秒)：",times)
            nums.append(times)
        # 调用统计函数
        num, means, medians, var = testcount.getcount(nums)
        print("总数：{},平均值:{:.2f},中位数:{:.2f},方差：{}".format(num, means, medians, var))

if __name__ == '__main__':

    ####数据修改刷新====
    ##03保持寄存器
    Fun().test2_read_hold()

    ####数据读取延时====
    ##02离散输入
    # Fun().test4_ls_input()
    ##04输入寄存器
    # Fun().test3_input_jc()



