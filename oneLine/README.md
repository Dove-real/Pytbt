# 一个没卵用的小尝试

## oneLine.py
每60s从三个一言站点获得文本信息，并保存到本地
1. https://v1.hitokoto.cn/
2. https://hitoapi.cc/sp/
3. https://api.satori.moe/hitokoto.php

非常感谢以上三个站点

## progressBar.py
像土拨鼠一样愚蠢的进度条显示模块

## oneLineMQTT.py
使用 oneLine.py 前一天获取到的文件

然后通过MQTT服务传递给物联网?设备

比如使用oneLineGet.py ↓

## oneLineGet.py
一个使用MQTT读取oneLine的简陋脚本
