# open(fileName,'wb') as f:
#   f.write()
'''
1.获取到下在的url,二进制方式下载
urllib,模块提供的urlretrieve()此模块可以进行音频文件下载
        也支持远程数据下载到本地
urlretrieve(url, filename=None, reporthook=None, data=None)

url:我们下载的下载url地址

filename:数据存储器路径_+文件名
reporthook:要求回调函数,链接上服务器或者响应数据下载完毕时触发该回调函数
            显示当前下载进度
data:(filename,headers)元组
'''

from urllib import request
import requests
import os
import random
from lxml import etree

User_Agents = [
    "Mozilla / 5.0(Linux;Android 4.1.1;Nexus 7 Build / JRO03D) AppleWebKit / 535.19(KHTML, like Gecko) Chrome / 18.0.1025.166 Safari / 535.19",
    "Mozilla / 5.0(Linux;U;Android 4.0.4;en - gb;GT - I9300 Build / IMM76D) AppleWebKit / 534.30(KHTML, like Gecko) Version / 4.0 Mobile Safari / 534.30",
    "Mozilla / 5.0(Linux;U;Android2.2;en - gb;GT - P1000 Build / FROYO) AppleWebKit / 533.1(KHTML, like Gecko) Version / 4.0 Mobile Safari / 533.1"
    "Mozilla / 5.0(Android;Mobile;rv: 14.0) Gecko / 14.0 Firefox / 14.0"
    "Mozilla / 5.0(iPad;CPU OS 5_0 like Mac OS X) AppleWebKit / 534.46(KHTML, like Gecko) Version / 5.1 Mobile / 9 A334 Safari / 7534.48.3"
    "Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3"
]
User_Agent = random.choice(User_Agents)
headers ={
    'User-Agent':User_Agent
}


url = "http://www.ivsky.com/bizhi/dongman/"

req = requests.get(url,headers=headers)
html = etree.HTML(req.text)
# print(req.text)
img_url = html.xpath('//div[@class="il_img"]//img/@src')
print(img_url)