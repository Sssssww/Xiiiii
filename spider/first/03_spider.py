'''
百度贴吧
https://tieba.baidu.com/f?ie=utf-8&kw=%E6%9D%8E%E6%AF%85
https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn=50
https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn=100
'''
from urllib import parse,request

# # 利用parse 进行转码
#
# # 将“李毅”转码
# kw = {'kw':"李毅"}
# a = parse.urlencode(kw)
# print(a)
# # 结果 :"kw=%E6%9D%8E%E6%AF%85"
#
# # 将编码后的数字转换回来
# b = parse.unquote(a)
# print(b)
# # 结果： "李毅"
url = "http://tieba.baidu.com/f?"
name = input("请输入贴吧名称:")
page = input("请输入贴吧页数:")
for i in range(int(page)):
    qs = {
        "kw":name,
        "pn":i*50
    }
    qs_data = parse.urlencode(qs)

    url = url+ qs_data
    # print(url)
    headers = {
        "User-Agent":"Mozilla / 5.0 (Windows NT 6.2;WOW64;rv: 21.0) Gecko / 2010010 Firefox / 21.0",
    }
    req = request.Request(url,headers=headers)

    rsp = request.urlopen(req)
    html = rsp.read().decode("utf-8")

    with open(name+"第"+str(i+1)+"页"+".html","w",encoding="utf-8") as f:
        f.write(html)