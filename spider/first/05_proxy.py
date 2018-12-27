from urllib import request
import random

# 代理
proxy_list = [
    {"http":"114.245.8.37:8060"},
    {"https":"119.179.60.117:8118"},
    # {"http":"115.219.107.42:8010"}

]

proxy = random.choice(proxy_list)

# 构建代理管理器
proxy_hander = request.ProxyHandler(proxy)


# 创建网络请求对象opener
opener = request.build_opener(proxy_hander)

url = "http://langlang2017.com"
headers = {
        "User-Agent":"Mozilla / 5.0 (Windows NT 6.2;WOW64;rv: 21.0) Gecko / 2010010 Firefox / 21.0",
    }

# 创建请求
req = request.Request(url,headers=headers)

rsp = opener.open(req)

content = rsp.read().decode()

print(content)