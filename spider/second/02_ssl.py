import requests


url = "https://www.12306.cn/index/"
rep = requests.get(url,verify = True)
# rep.encoding = rep.apparent_encoding    # 解决页面乱码
print(rep.text)