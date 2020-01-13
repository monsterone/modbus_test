from mqtt.pub_sub import main1, main2,main3
import os,json
import configparser as cparser


'''配置文件加载'''
base_dir = str(os.path.dirname(__file__))
file_path = base_dir + "/tools/config.ini"
cf = cparser.ConfigParser()
cf.read(file_path, encoding='utf-8')
##子设备前缀
mid = cf.get("DEVICE", "MID")


'''json文件加载'''
with open(os.path.dirname(__file__) + '/tools/mq.json', 'r', encoding='utf8') as f:
    datas = json.load(f)
#订阅读数据
read = json.dumps(datas['read'])
#订阅写数据
write = json.dumps(datas['write'])



##订阅发布
def keep(id=18,type='read'):
    id = str(id)
    response = "response/"+str(id)+"/"+mid + id
    command = "command/"+str(id)+"/"+mid + id
    if type == 'read' :
        q = main2(response,command,read)
        return q
    elif type == 'write':
        q = main2(response,command,write)
        return q

##发布
def keep2(id=18,type='read'):
    id = str(id)
    response = "response/" + str(id) + "/" + mid + id
    command = "command/" + str(id) + "/" + mid + id
    q = main3(command,read)
    return q

