import time
import unittest
from HTMLTestRunnerCN import HTMLTestReportCN

#构建测试集
test_dir = './case/'
suite = unittest.defaultTestLoader.discover(test_dir, pattern="percase1.py")

#构建测试集
# suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

# 定义报告生成路径
report_path = '.' + '/report/'
# 格式化时间
now_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(time.time()))
# 测试报告生成格式
HtmlFile = report_path + now_time + "result.html"


if __name__ == '__main__':

    ####################生成报告#################
    # 生成测试报告
    with open(HtmlFile, 'wb+') as f:
        HTMLTestReportCN(
            stream=f, title="modbus测试报告", description="用例执行情况",tester="Rex109").run(suite)


    ####################发邮件#################
    # # 测试报告目录
    # new_path = report_path
    # # 查找最新的测试报告文件
    # rp=Report()
    # new_report = rp.get_new_file(new_path)
    # # 发送测试报告，带附件
    # rp.send_mail_attr(new_report)
