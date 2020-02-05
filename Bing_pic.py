#用于爬取Bing首页背景，获得5K分辨率图片。
import requests
import re
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
html=requests.get('https://cn.bing.com/',headers=header).text
img_id=re.findall(r'.*?background-image:url\((.*?)&.*?',html)
img_fhd=img_id[0]
img_uhd=img_fhd.replace('1920x1080','UHD')
img_url="https://cn.bing.com"+img_uhd
print(img_url)
name='qwq.jpg'
img=requests.get(img_url)
with open(name,'wb') as f:
   f.write(img.content)
   f.close()