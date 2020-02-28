import json
import sys
import time
import random
import datetime
import paho.mqtt.client

aliHOST = "xxx.xxx.xxx.xxx"
aliPORT = 1883
clitntID  = "pyOneLineClient_"


def on_connect(client, userdata, flags, rc):
    print("连接服务器: " + str(rc))
    client.subscribe("hjOneLinePut")
    print("订阅 hjOneLinePut: " + str(rc))
    print (" ")
    print (" ",flush=True)

def on_message(client, userdata, msg):
    objson = json.loads(str(msg.payload,'utf-8'))
    txt = objson["text"]
    author = objson["anthor"]
    if len(author) > 0 :
        print (txt + "  -- " + author)
    else:
        print (txt)
    print (" ",flush=True)

def mqtt_start():
    client.username_pw_set("hjpc","htxzdj")
    client.on_connect = on_connect
    client.on_message  = on_message
    client._client_id = clitntID + str(hex(random.randint(0,0xffffffff)))   #产生随机clientID
    client.connect(aliHOST,aliPORT,60)
    print ("pyOneLineServer 初始化结束, 等待请阅请求",flush = True)
    client.loop_start()

if __name__ == "__main__":
    client = paho.mqtt.client.Client(transport='tcp')
    mqtt_start()
    while True:
        client.publish(topic='hjOneLineGet',payload="text")
        time.sleep(2) #不要小于0.1,否则会发生很多丢包情况
    quit()

