import requests
import re
import time
from xlutils.copy import copy
from xlrd import open_workbook
url_original = r"https://s.taobao.com/search?q=%E9%81%BF%E5%AD%95%E5%A5%97"
headers = {
    'Host': 's.taobao.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4052.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'referer': 'https://s.taobao.com/search?q=%E9%81%BF%E5%AD%95%E5%A5%97&bcoffset=-5&p4ppushleft=%2C48&s=616&ntoffset=-5',
    'Cookie': 'thw=cn; cna=0JHFFixILSsCAd6MivYNIWY7; t=e91f89cb9c3883b6199aa35a420e05ab; cookie2=42426ad7a02706cb3cc8c67a817553ee; v=0; _tb_token_=ee83be73eeb75; _samesite_flag_=true; lgc=tb836375343; dnk=tb836375343; tracknick=tb836375343; tg=0; enc=igHXd0AvsTppX6aTDBZcZtvZzHf6d7JzeLLMdVypymVmyQOODtRRg25AmMyhoOhwAAtSzfjOW8XFLc6WFB9CqA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=104_1; _uab_collina=158122041049921755491714; x5sec=7b227365617263686170703b32223a226136306330663563363764343163306438623435366539323333343134356532434c79452f76454645496e32682f2b5770364f6a50686f4d4d7a67774d6a59314d446b324e447378227d; JSESSIONID=6E1AE48DC92A3EC410DA47FD3C4B62F8; unb=3802650964; uc1=cookie14=UoTUO8IQPKs0uw%3D%3D&tag=8&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&lng=zh_CN&pas=0&existShop=false&cookie21=UIHiLt3xThH8t7YQoFNq&cookie15=W5iHLLyFOGW7aA%3D%3D; uc3=vt3=F8dBxdsamFKEAW7H%2BgY%3D&nk2=F5RNZqrONCc2DFw%3D&lg2=W5iHLLyFOGW7aA%3D%3D&id2=UNiE4KkG7RL%2BvQ%3D%3D; csg=16f7fcac; cookie17=UNiE4KkG7RL%2BvQ%3D%3D; skt=25c7e96f91662902; existShop=MTU4MTIyMDczOA%3D%3D; uc4=id4=0%40Ug%2BbVNOJJ7YM04aLwZEgSOUM92uQ&nk4=0%40FY4GsXBaaZlHc8%2FNrrmkbQfUiYFbxQ%3D%3D; _cc_=VFC%2FuZ9ajQ%3D%3D; _l_g_=Ug%3D%3D; sg=34f; _nk_=tb836375343; cookie1=BxE1uVugdyXr6%2FgtRnXnuz002ARt%2BhQxwKLAM0NWZ%2FQ%3D; l=cBMTD3ZmQbCDXIKSKOCwourza77OSIRAguPzaNbMi_5ZE6L19i_Oo2bKsFp6VfWdOY8B4TRL92v9-etkiJK5QsA8E5vP.; isg=BOnpxrNakyc03a-TePTnwBCd-JVDtt3orPAqYIveZVAPUglk0wbtuNdAEP7kSnUg'
}
# 阿里验证码无法处理，此处使用Cookie来解决。
def get_detail():
    response = requests.get(url, headers=headers).text
    nid =re.findall(r'nid":"(.*?)"',response)
    name=re.findall(r'"raw_title":"(.*?)"',response)
    price=re.findall(r'"view_price":"(.*?)"',response)
    sales=re.findall(r'"view_sales":"(.*?)人付款"',response)
    item=0;
    num=min(len(nid),len(name),len(price),len(sales))
    while(item<=num-1):
        print(nid[item],' ',name[item],' ',price[item],' ',sales[item])
        item=item+1

    rexcel=open_workbook("py.xls")
    rows=rexcel.sheets()[0].nrows
    excel=copy(rexcel)
    sheet=excel.get_sheet(0)
    j=0
    for i in range(rows+1,rows+num):
        sheet.write(i,0,nid[j])
        sheet.write(i,1,name[j])
        sheet.write(i,2,price[j])
        sheet.write(i,3,sales[j])
        j=j+1
    excel.save("py.xls")
    
for i in range(3,60):
    url=url_original+"&s="+str(i*44)
    print("这是第",i+1,"页数据")
    get_detail()
    time.sleep(10)

