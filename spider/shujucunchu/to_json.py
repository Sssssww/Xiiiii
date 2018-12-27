"""
python 对json文件操作分为编码和解码
dumps   字符串
dump    json对象  可以通过fp文件流写入

解码：
    loads
    load
"""
import requests,json
from bs4 import BeautifulSoup
headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
}
r = requests.get('http://www.seputu.com/',headers=headers)
# print(r.text)

soup =BeautifulSoup(r.text,"lxml")
content = []
for mulu in soup.find_all(class_="mulu"):  #  凡是写在[ ]里面的都是class，外面的class_
    # print(mulu)
    h2 = mulu.find('h2')
    if h2 != None:
        h2_title = h2.string
        # print(h2_title)
        list_1 = []
        for a in mulu.find(class_="box").find_all('a'):
            herf = a.get('href')
            box_title = a.get('title')
            print(herf,box_title)
            list_1.append({"herf":herf,"box_title":box_title})
        content.append("title":h2_title,"cotent":list_1)
with open("gcd.json",'a'.encoding=('utf-8')) as fp:# a 代表以流的方式进行
    json.dump(content,fp=fp,indent=4,ensure_ascii=False) # indent 可以令格式个清楚