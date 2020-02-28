import json
import sys
import time
import datetime
import random
import paho.mqtt.client
from apscheduler.schedulers.background import BackgroundScheduler

aliHOST = "127.0.0.1"
aliPORT = 1883
clitntID  = "pyOneLineServer"

oneLineFileDir = "" #文件路径全局变量
oneLineFileLen = 0  #文件长度全局变量

def on_connect(client, userdata, flags, rc):
    print("连接服务器: " + str(rc),flush = True)
    client.subscribe("hjOneLineGet")
    print("订阅 hjOneLineGet: " + str(rc),flush = True)

def on_message(client, userdata, msg):
    print("收到订阅 hjOneLineGet 主题: " + str(msg.payload),flush = True)
    text = radomLine()
    client.publish(topic='hjOneLinePut',payload=text)

def mqtt_start():
    client = paho.mqtt.client.Client(transport='tcp')
    client.username_pw_set("hjpc","htxzdj")
    client.on_connect = on_connect
    client.on_message  = on_message
    client._client_id = clitntID
    client.connect(aliHOST,aliPORT,60)
    #client.publish('hjOneLineGet',payload='',qos = 0)
    print ("pyOneLineServer 初始化结束, 等待请阅请求",flush = True)
    client.loop_forever()
    

def openFile():
    dir = time.strftime("%Y-%m-%d %H:%M:%S",(time.localtime(time.time()-86400)))
    dir = "./saveFile/Hitokoto" + dir[:10] + ".txt"
    global oneLineFileDir
    oneLineFileDir = dir
    try:
        with open(dir,"r",encoding = "utf-8") as f:
            print ("open file OK",flush = True)
    except:
        print ("open file error",flush = True)
        quit()


def radomLine():    #随机取一行
    l = random.randint(1,(oneLineFileLen-2))
    dir = oneLineFileDir
    print ("Textdur :" + oneLineFileDir,flush = True)
    with open(dir,"r",encoding = "utf-8") as oneLineFile:
        line = oneLineFile.readlines()[l]
        return line

#@sc.scheduled_job('cron', day_of_week='*', hour=14, minute='22', second='30')
def check_db():
    print("\n定时检查oneLine文件",flush = True)
    dir = time.strftime("%Y-%m-%d %H:%M:%S",(time.localtime(time.time()-86400)))
    dir = "./saveFile/Hitokoto" + dir[:10] + ".txt"
    global oneLineFileDir
    try:
        with open(dir,"r",encoding = "utf-8") as f:
            print ("发现新文件",flush = True)
            oneLineFileDir = dir
            print ("当前文件 :" + oneLineFileDir,flush = True)
    except:
        print ("未发现新文件, 仍使用当前文件",flush = True)
        print ("当前文件 :" + oneLineFileDir,flush = True)


if __name__ == "__main__":  #程序载入文件并读取文件长度
    openFile()
    oneLineFileLen = 0
    print ("dir:" + oneLineFileDir,flush = True)
    dir = oneLineFileDir
    
    bkScheduler = BackgroundScheduler()
    bkScheduler.add_job(check_db,'cron', day_of_week='*', hour=0, minute=00, second=30)
    try:
        bkScheduler.start()
        print("定时任务设定",flush =True)
    except Exception as e:
        bkScheduler.shutdown()
        print("定时错误",flush =True)
    finally:
        print("定时完成",flush =True)

    with open(dir,"r",encoding = "utf-8") as oneLineFile:
        oneLineFileLen = len(oneLineFile.readlines())
        print ("LineNumber: %d" % oneLineFileLen)
        print ("测试 :" + radomLine(),flush = True)
    
    mqtt_start()
    #发生错误：
    print ("MQTT 异常, 停止运行",flush = True)
    quit()


