本脚本实现的功能是抓取Bing首页背景图片并以年月日命名保存到工作目录下，通过对URL的修改来获取当天最高分辨率图片（UHD+)。同时，抓取完成后会通过[server酱](http://sc.ftqq.com/3.version)完成推送到微信上的功能，因此你需要前去申请Sckey。

食用方法如下：

* 修改Bing_pic.py中`requests.post('https://sc.ftqq.com/{Key}.send', data=data)`这段中的{Key}为你在[server酱](http://sc.ftqq.com/3.version)上申请的Sckey，注意最终的链接中没有花括号。

* `pip3 install requests`

* `pip3 install pillow`

* `python3 Bing_pic.py`

* 使用`crontab`命令，将Python脚本加入Linux任务计划。