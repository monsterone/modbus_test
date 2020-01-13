import random

from mqtt.pub_sub import connect_mqtt
from performance.case2.dofunc import FunBus
from time import sleep




'''稳定性'''
def longrun():

    ##连接mqtt
    connect_mqtt()
    while True:
        ##产生一个随机函数
        beg = random.randint(1,5)
        # print(beg)
        #读-线圈
        if beg == 1:
            FunBus().test6_read_coil()
            sleep(1)
        #写-线圈
        elif beg == 2:
            FunBus().test5_write_coil()
            sleep(2)
        #读-离散输入
        elif beg == 3:
            FunBus().test4_ls_input()
            sleep(3)
        #读-输入寄存器
        elif beg == 4:
            FunBus().test3_input_jc()
            sleep(4)
        #读-保持寄存器
        elif beg == 5:
            FunBus().test2_read_hold()
            sleep(5)
        #写-保持寄存器
        elif beg == 6:
            FunBus().test1_write_hold()
            sleep(6)


