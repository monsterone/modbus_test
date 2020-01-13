import time


def timefor():
    time1  = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    return time1