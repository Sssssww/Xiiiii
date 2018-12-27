from urllib import request

isproxy = input("plese iuput is adency y/n:")

# 有代理
proxy_1 = request.ProxyHandler({"http":"114.245.8.37:8060"})
# 无代理
proxy_2 = request.ProxyHandler()

if isproxy == "y":
    opener = request.build_opener(proxy_1)



headers = {
        "User-Agent":"Mozilla / 5.0 (Windows NT 6.2;WOW64;rv: 21.0) Gecko / 2010010 Firefox / 21.0",
    }
url = "http://www.langlang2017.com"
req = request.Request(url,headers=headers)
rsp = opener.open(req)

print(rsp)
