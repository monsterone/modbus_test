import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md


class ModbusClient():

    def __init__(self):
        # 远程连接到服务器端
        self.master = mt.TcpMaster("192.168.1.230", 502)
        self.master.set_timeout(5.0)

        # @slave=1 : identifier of the slave. from 1 to 247.  0为广播所有的slave
        # @function_code=READ_HOLDING_REGISTERS：功能码
        # @starting_address=1：开始地址
        # @quantity_of_x=3：寄存器/线圈的数量
        # @output_value：一个整数或可迭代的值：1/[1,1,1,0,0,1]/xrange(12)
        # @data_format
        # @expected_length

    ###---------读操作------------###
    # 01读线圈状态(00001-09999),位，单个或多个
    def READ_COILS(self, starting_address, quantity_of_x):
        READ_COILS = self.master.execute(
            slave=1,
            function_code=md.READ_COILS,
            starting_address=starting_address,
            quantity_of_x=quantity_of_x)
        return READ_COILS

    # 02读离散输入(10001-19999).位，单个或多个
    def READ_DISCRETE_INPUTS(self, starting_address, quantity_of_x):
        READ_DISCRETE_INPUTS = self.master.execute(
            slave=1,
            function_code=md.READ_DISCRETE_INPUTS,
            starting_address=starting_address,
            quantity_of_x=starting_address)
        return READ_DISCRETE_INPUTS

    # 04读输入寄存器(30001-39999).字，单个或多个
    def READ_INPUT_REGISTERS(self, starting_address, quantity_of_x):
        READ_INPUT_REGISTERS = self.master.execute(
            slave=1,
            function_code=md.READ_INPUT_REGISTERS,
            starting_address=starting_address,
            quantity_of_x=quantity_of_x)
        return READ_INPUT_REGISTERS

    # 03读保存寄存器(40001-49999).字，单个或多个
    def READ_HOLDING_REGISTERS(self, starting_address, quantity_of_x):
        READ_HOLDING_REGISTERS = self.master.execute(
            slave=1,
            function_code=md.READ_HOLDING_REGISTERS,
            starting_address=starting_address,
            quantity_of_x=quantity_of_x)
        return READ_HOLDING_REGISTERS

    ###---------写操作------------###

    # 05写单个线圈，位
    def WRITE_SINGLE_COIL(self,starting_address,quantity_of_x,output_value):
        WRITE_SINGLE_COIL = self.master.execute(
            slave=1,
            function_code=md.WRITE_SINGLE_COIL,
            starting_address=starting_address,
            quantity_of_x=quantity_of_x,
            output_value=output_value)
        # return WRITE_SINGLE_COIL

    # 15写多个线圈，位
    def WRITE_MULTIPLE_COILS(
            self,
            starting_address,
            quantity_of_x,
            output_value):
        WRITE_MULTIPLE_COILS = self.master.execute(
            slave=1,
            function_code=md.WRITE_MULTIPLE_COILS,
            starting_address=starting_address,
            quantity_of_x=quantity_of_x,
            output_value=output_value)
        return WRITE_MULTIPLE_COILS

    # 06写单个保存寄存器，字
    def WRITE_SINGLE_REGISTER(
            self,
            starting_address,
            quantity_of_x,
            output_value):
        WRITE_SINGLE_REGISTER = self.master.execute(
            slave=1,
            function_code=md.WRITE_SINGLE_REGISTER,
            starting_address=starting_address,
            quantity_of_x=quantity_of_x,
            output_value=output_value)
        # return WRITE_SINGLE_REGISTER

    # 16写多个保存寄存器，字
    def WRITE_MULTIPLE_REGISTERS(
            self,
            starting_address,
            quantity_of_x,
            output_value):
        WRITE_MULTIPLE_REGISTERS = self.master.execute(
            slave=1,
            function_code=md.WRITE_MULTIPLE_REGISTERS,
            starting_address=starting_address,
            quantity_of_x=quantity_of_x,
            output_value=output_value)
        return WRITE_MULTIPLE_REGISTERS

if __name__ == '__main__':
    mb = ModbusClient()
    #读圈
    # data1 = mb.READ_COILS(0,10)
    data1 = mb.WRITE_SINGLE_COIL(0,1,1)
    print(data1)