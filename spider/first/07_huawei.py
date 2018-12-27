"""
urllic 模拟华为官网登录
# 登录接口 有些可以在form 表单中查找
#  form 表单查找不到时 可以输入一个真确的账号错误的密码去获取 登录接口
url ="https://www.huawei.com/en/accounts/LoginPost"
method:post
form :
    userName:3166801236@qq.com
    pwd:mS2s7JhyvBcqVhM0nbRMl7cRgWTeTZnJJI3MWI5Yx09EgoW4b99YCAsnGWtJVzvd7kn2ooG+BGXjeCcSqt6jjGjGSRU4tSQBqzq+H/j3/7wNjh26DskmfD91IPN2EkZjAamQGzq+X6aKDUrZ0CCy5OIL1oy7w7ya7t6CKGbGojs=
    languages:zh
    fromsite:www.huawei.com
    authMethod:password
"""

from urllib import request,parse
from http import  cookiejar

url ="https://www.huawei.com/en/accounts/LoginPost"

# 生成cookie对象
cookie = cookiejar.CookieJar()

# 生成cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 生成http管理器
http_handler = request.HTTPHandler()
# 生成http请求管理器
https_handler =  request.HTTPSHandler()
# 构建发起请求的管理器
opener = request.build_opener(cookie_handler,http_handler,https_handler)



# 构建登录函数
def login(url):
    data = {
        "userName":"3166801236@qq.com",
        "pwd":"a789520.",
        "languages":"zh",
        "fromsite":"www.huawei.com",
        "authMethod":"password",

    }
    data = parse.urlencode(data)
    # 请求登录 data数据类型传入需要是bytes
    req = request.Request(url, data = bytes(data,"utf-8"))
    # 发起请求
    content = opener.open(req)
    content = content.read().decode("utf-8")
    print(content)

if __name__ == '__main__':
    url = "https://www.huawei.com/en/accounts/LoginPost"
    login(url)