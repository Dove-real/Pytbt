# encoding:'utf-8'
import urllib.request
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re
import os
import time
import codecs
import json
import requests
# 找到网址


def getDatas(url,):
    ua = UserAgent()
    header = {'User-Agent': ua.random}
    ret = urllib.request.Request(url=url, headers=header)
    # 打开网页
    res = urllib.request.urlopen(ret)
    # 转化格式
    response = BeautifulSoup(res, 'html.parser')
    # 找到想要数据的父元素
    datas = response.find_all('p')
    datas_subject = response.h1
    # 创建存放数据的文件夹
    folder_name = "output"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    # 定义文件
    file_name = "0-1000"+".json"
    # 文件路径
    file_path = folder_name+"/"+file_name

    millis = int(round(time.time() * 1000))

    for item in datas:
        item_re = str(item)
        if re.findall(r'.*?&gt;(.*?)<br/>.*?', item_re):
            dict1 = {}
            dict1['subject'] = str(datas_subject.get_text())
            dict1['topic'] = re.findall(r'.*?&gt;(.*?)<br/>.*?', item_re)
            dict1['answers'] = re.findall(r'.*?<br/>(.*)<br/>.*?', item_re)
            dict1['correct'] = item.find('code').get_text()
            dict1['time'] = str(millis)
            # 保存数据为json格式

            try:
                with codecs.open(file_path, 'a', encoding="utf-8") as fp:
                    fp.write(json.dumps(dict1, ensure_ascii=False)+",\n")
            except IOError as err:
                print('error'+str(err))
            finally:
                fp.close()


i = 0
while(i <= 1000):
    url = 'http://www.datiwuyou.com/chaoxingerya/'+str(i)+'.html'
    print(url)
    getDatas(url)
    time.sleep(1)
    if i % 100 == 0:
        time.sleep(30)
    i = i+1
    if i % 100 == 0:
        data = {
            'text': str(i)
        }
        requests.post(
            'https://sc.ftqq.com/{Key}.send', data=data
        )
