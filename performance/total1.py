from performance.case1.percase1 import Fun

'''modbus统计'''



'''数据修改刷新'''

## 01线圈刷新
# Fun().test6_read_coil()
##03保持寄存器刷新
Fun().test2_read_hold()




'''数据读取延时'''

##02离散输入
# Fun().test4_ls_input()
##04输入寄存器
# Fun().test3_input_jc()