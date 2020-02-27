import json
import os
import time
import re
import requests
from requests.exceptions import ReadTimeout,ConnectTimeout
# from apscheduler.schedulers.background import BackgroundScheduler

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
nowTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

def saveToFile(obJsonText):
    dir = "./saveFile/Hitokoto" + nowTime[:10] + ".txt"
    f = open(dir, "a+", encoding="utf-8")
    f.write("\n")
    f.write(obJsonText)
    f.close()

def getOneLineHitokoto():
    try:
        get = requests.get("https://v1.hitokoto.cn/",headers=headers, timeout=2)
        objson = json.loads(get.text)
        if objson != '':
            txt = objson["hitokoto"]
            author = objson["from"]
            if len(author) > 0 :
                print (txt + " --" + author)
            else:
                print (txt)

            obJsonText = "{\"from\":\"hitokoto.cn\",\"text\":\"" + txt + "\",\"anthor\":\"" + author + "\"}"
            saveToFile (obJsonText.replace("\n", ""))

    except ReadTimeout:
        print('Yiju: Timeout')
    except ConnectTimeout:
        print('Yiju: ConnectTimeout')


def getHitoApiHitokoto():
    try:
        get = requests.get("https://hitoapi.cc/sp/",headers=headers, timeout=2)
        objson = json.loads(get.text)
        if objson != '':
            txt = objson["text"]
            author = objson["author"]
            if len(author) > 0 :
                print (txt + " --" + author)
            else:
                print (txt)
        
            obJsonText = "{\"from\":\"hitoapi.cc\",\"text\":\"" + txt + "\",\"anthor\":\"" + author + "\"}"
            saveToFile (obJsonText.replace("\n", ""))

    except ReadTimeout:
        print('Hitoapi: Timeout')
    except ConnectTimeout:
        print('Hitoapi: ConnectTimeout')


def getSatoriHitokoto():
    try:
        get = requests.get("https://api.satori.moe/hitokoto.php",headers=headers, timeout=2)
        objson = json.loads(get.text)
        if objson != '':
            txt = objson["hitokoto"]
            author = objson["source"]
            if len(author) > 0 :
                print (txt + " --" + author)
            else:
                print (txt)

            obJsonText = "{\"from\":\"satori.moe\",\"text\":\"" + txt + "\",\"anthor\":\"" + author + "\"}"
            saveToFile (obJsonText.replace("\n", ""))

    except ReadTimeout:
        print('Satori: Timeout')
    except ConnectTimeout:
        print('Satori: ConnectTimeout')
    

if __name__ == "__main__":
    while True :
        nowTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        print (nowTime)

        getOneLineHitokoto()
        getSatoriHitokoto()
        getHitoApiHitokoto()
        print (' ',flush=True)

        time.sleep(40)
