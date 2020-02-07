# 用于爬取Bing首页背景，获得UHD+分辨率的图片。
import requests
import re
import time
from PIL import Image
import os
# 使用本机UA
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
html = requests.get('https://cn.bing.com/',
                    headers=header).text  # 获取Bing首页html源码

# 正则表达式寻找图片URL并更改为高分辨率图片地址
img_id = re.findall(r'.*?background-image:url\((.*?)&.*?', html)
img_fhd = img_id[0]
img_uhd = img_fhd.replace('1920x1080', 'UHD')
img_url = "https://cn.bing.com"+img_uhd
print(img_url)

name = time.strftime('%Y%m%d')+'.jpg'  # 以年月日命名图片
img = requests.get(img_url)
with open(name, 'wb') as f:
    f.write(img.content)
    f.close()
print('Save as', name)

# 获取图片尺寸
path = os.path.join(os.getcwd(), name)
img = Image.open(path)

data = {
    'text': 'Bing首页图片已抓取',
    'desp': name+str(img.size)
}
requests.post(
    'https://sc.ftqq.com/{Key}.send', data=data)
