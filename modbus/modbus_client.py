import modbus_tk
import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md


try:
    # 远程连接到服务器端
    master = mt.TcpMaster("192.168.1.230", 502)
    master.set_timeout(5.0)

    # @slave=1 : identifier of the slave. from 1 to 247.  0为广播所有的slave
    # @function_code=READ_HOLDING_REGISTERS：功能码
    # @starting_address=1：开始地址
    # @quantity_of_x=3：寄存器/线圈的数量
    # @output_value：一个整数或可迭代的值：1/[1,1,1,0,0,1]/xrange(12)
    # @data_format
    # @expected_length

    ###---------读操作------------###
    ##01读线圈状态(00001-09999),位，单个或多个
    READ_COILS = master.execute(slave=1, function_code=md.READ_COILS, starting_address=0, quantity_of_x=3)

    ##02读离散输入(10001-19999).位，单个或多个
    READ_DISCRETE_INPUTS = master.execute(slave=1, function_code=md.READ_DISCRETE_INPUTS, starting_address=0, quantity_of_x=3)

    ##04读输入寄存器(30001-39999).字，单个或多个
    READ_INPUT_REGISTERS = master.execute(slave=1, function_code=md.READ_INPUT_REGISTERS, starting_address=0, quantity_of_x=3)

    ##03读保存寄存器(40001-49999).字，单个或多个
    READ_HOLDING_REGISTERS = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=0, quantity_of_x=3)


    ###---------写操作------------###

    ##05写单个线圈，位
    WRITE_SINGLE_COIL = master.execute(slave=1, function_code=md.WRITE_SINGLE_COIL, starting_address=0, quantity_of_x=8,output_value=range(1,12))

    ##15写多个线圈，位
    WRITE_MULTIPLE_COILS = master.execute(slave=1, function_code=md.WRITE_MULTIPLE_COILS, starting_address=0, quantity_of_x=8,output_value=range(1,12))


    ##06写单个保存寄存器，字
    WRITE_SINGLE_REGISTER = master.execute(slave=1, function_code=md.WRITE_SINGLE_REGISTER, starting_address=0, quantity_of_x=8,output_value=range(1,12))

    ##16写多个保存寄存器，字
    WRITE_MULTIPLE_REGISTERS = master.execute(slave=1, function_code=md.WRITE_MULTIPLE_REGISTERS, starting_address=0, quantity_of_x=8,output_value=range(1,12))



    Hold_value = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=0, quantity_of_x=3,
                                output_value=5)

    Coils_write = master.execute(slave=1, function_code=md.WRITE_MULTIPLE_COILS, starting_address=0, quantity_of_x=8,output_value=range(1,12))
    Coils_value = master.execute(slave=1, function_code=md.READ_COILS, starting_address=0, quantity_of_x=15)


    print(Coils_write)
    print(Hold_value)  # 取到的寄存器的值格式为元组(55, 12, 44)
    print(Coils_value)  # 取到的寄存器的值格式为元组(1, 1, 1)

except modbus_tk.modbus.ModbusError as e:
        print("%s- Code=%d" % (e, e.get_exception_code()))