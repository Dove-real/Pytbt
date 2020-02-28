import json
import os
import time
import re
import requests
from requests.exceptions import ReadTimeout,ConnectTimeout

import progressBar

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
            txt = objson["hitokoto"].replace('\n','')
            author = objson["from"].replace('\n','')
            txt = txt.replace('\r','')
            author = author.replace('\r','')
            if len(author) > 0 :
                print (txt + " --" + author,flush=True)
            else:
                print (txt,flush=True)

            obJsonText = "{\"from\":\"hitokoto.cn\",\"text\":\"" + txt + "\",\"anthor\":\"" + author + "\"}"
            saveToFile (obJsonText)

    except ReadTimeout:
        print('Yiju: Timeout',flush=True)
    except ConnectTimeout:
        print('Yiju: ConnectTimeout',flush=True)


def getHitoApiHitokoto():
    try:
        get = requests.get("https://hitoapi.cc/sp/",headers=headers, timeout=2)
        objson = json.loads(get.text)
        if objson != '':
            txt = objson["text"].replace('\n','')
            author = objson["author"].replace('\n','')
            txt = txt.replace('\r','')
            author = author.replace('\r','')
            if len(author) > 0 :
                print (txt + " --" + author,flush=True)
            else:
                print (txt,flush=True)
        
            obJsonText = "{\"from\":\"hitoapi.cc\",\"text\":\"" + txt + "\",\"anthor\":\"" + author + "\"}"
            saveToFile (obJsonText)

    except ReadTimeout:
        print('Hitoapi: Timeout',flush=True)
    except ConnectTimeout:
        print('Hitoapi: ConnectTimeout',flush=True)


def getSatoriHitokoto():
    try:
        get = requests.get("https://api.satori.moe/hitokoto.php",headers=headers, timeout=2)
        objson = json.loads(get.text)
        if objson != '':
            txt = objson["hitokoto"].replace('\n','')
            author = objson["source"].replace('\n','')
            txt = txt.replace('\r','')
            author = author.replace('\r','')
            if len(author) > 0 :
                print (txt + " --" + author,flush=True)
            else:
                print (txt,flush=True)

            obJsonText = "{\"from\":\"satori.moe\",\"text\":\"" + txt + "\",\"anthor\":\"" + author + "\"}"
            saveToFile (obJsonText)

    except ReadTimeout:
        print('Satori: Timeout',flush=True)
    except ConnectTimeout:
        print('Satori: ConnectTimeout',flush=True)
    

if __name__ == "__main__":
    while True :
        nowTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        print (nowTime)

        getOneLineHitokoto()
        getSatoriHitokoto()
        getHitoApiHitokoto()

        delayTime = 40
        for i in range(0, delayTime*4):
            progressBar.setBar(i, delayTime*4)
            time.sleep(0.25)
        progressBar.clearBar()
        print('', flush=True)
