"""
http://www.langlang2017.com/index.html
http://www.langlang2017.com/route.html
http://www.langlang2017.com/FAQ.html
"""
from urllib import request
import random

def spider(url):
    user_Agent_list = [
        "Mozilla / 5.0 (Windows NT 6.2;WOW64;rv: 21.0) Gecko / 2010010 Firefox / 21.0",
        "Mozilla / 5.0(Windows NT 6.2;WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 27.0.1453.94 Safari / 537.36",
        "Mozilla / 5.0(Linux; Android 4.0.4; Galaxy Nexus Build / IMM76B) AppleWebKit / 535.19(KHTML, like Gecko) Chrome / 18.0.1025.133 Mobile Safari / 535.19",
        "Mozilla / 5.0(Linux;Android 4.1.1;Nexus 7 Build / JRO03D) AppleWebKit / 535.19(KHTML, like Gecko) Chrome / 18.0.1025.166 Safari / 535.19",
        "Mozilla / 5.0(Linux;U;Android 4.0.4;en - gb;GT - I9300 Build / IMM76D) AppleWebKit / 534.30(KHTML, like Gecko) Version / 4.0 Mobile Safari / 534.30",
        "Mozilla / 5.0(Linux;U;Android2.2;en - gb;GT - P1000 Build / FROYO) AppleWebKit / 533.1(KHTML, like Gecko) Version / 4.0 Mobile Safari / 533.1"
    ]
    # 随机从user_Agent_list中取一个user-agent
    user_agent = random.choice(user_Agent_list)
    # 构建haeader头信息
    headers = {
        'User-Agent':user_agent
    }
    req = request.Request(url=url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()

    # print(html)

    # 构建文件名
    name = url.split('/')
    fileName = 'TL_' + name[-1]
    # print(fileName)
    with open (fileName,'w',encoding = 'utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    url_list = [
        "http://www.langlang2017.com/index.html",
        "http://www.langlang2017.com/route.html",
        "http://www.langlang2017.com/FAQ.html"
    ]

    for url in url_list:
        spider(url)

