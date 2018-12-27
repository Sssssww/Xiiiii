'''
w3c资料爬取
url = 'http://www.w3school.com.cn/json/index.asp'
method:get
'''
# from urllib import request
# url = 'http://www.w3school.com.cn/json/index.asp'
# req = request.urlopen(url)
# rsp = req.read().decode("gb2312")  # 编码类型在 网页F12 elements上查看
# print(rsp)


from urllib import error,request

try:
    base_url = "http://www.w3school.com.cn/json/index.asp"
    rsp = request.urlopen(base_url)
    content = rsp.read().decode("utf-8")
    print(content)
except error.HTTPError as e:
    print(e)
except error.URLError as e:
    print(e)
except Exception as e:
    print(e)