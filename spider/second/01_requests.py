import requests

url = "https://item.jd.com/1250438.html"

try:
    rep = requests.get(url)
    print(rep.status_code)          # 打印状态码 如200 ，404
    print(rep.url)                  # 打印url地址
    print(rep.apparent_encoding)    # 打印原文编码类型
    rep.encoding = rep.apparent_encoding    #解决页面乱码
    print(type(rep.text))           # 响应得到字符串
    print(type(rep.content))        # 响应得到bytes
    print(rep.content)
    # print(rep.text)               #  请求html
    Cookiejar = rep.cookies         # 返回cook对象
    print(Cookiejar)
    cookiedick = requests.utils.dict_from_cookiejar(Cookiejar)
    print(cookiedick)
except:
    print("爬取失败")