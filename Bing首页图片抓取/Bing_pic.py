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
                    headers=header).text

# 正则表达式寻找图片URL并尝试将之更改为高分辨率图片地址
img_id = re.findall(r'.*?background-image:url\((.*?)&.*?', html)
img_fhd = img_id[0]
img_uhd = img_fhd.replace('1920x1080', 'UHD')
img_url = "https://cn.bing.com"+img_uhd
print(img_url)

# 以年月日命名图片，并储存到本地。
name = time.strftime('%Y%m%d')+'.jpg'
img = requests.get(img_url)
with open(name, 'wb') as f:
    f.write(img.content)
    f.close()
print('Save as', name)

# 获取图片尺寸
path = os.path.join(os.getcwd(), name)
img_file = Image.open(path)

# 异常情况处理，即当天图片不符合要求，一般出现在当天背景为MP4的情况下
if(img_file.width < 250):
    img_url = "https://cn.bing.com"+img_fhd
    img = requests.get(img_url)
    with open(name, 'wb') as f:
        f.write(img.content)
        f.close()
    print('Save as', name)
    img_file = Image.open(path)

# 通过ServerChan发送通知到微信
data = {
    'text': 'Bing首页图片已抓取',
    'desp': name+str(img_file.size)
}
requests.post(
    'https://sc.ftqq.com/SCU27489T31134321f69b92ae24bbc79292576a945b152d2f41663.send', data=data
)
