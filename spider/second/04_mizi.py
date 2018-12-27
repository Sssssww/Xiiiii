import requests
import random
import os
from lxml import etree

def html_1(base_url):
    # base_url = "http://www.mzitu.com/"
    User_Agents = [
        "Mozilla / 5.0(Linux;Android 4.1.1;Nexus 7 Build / JRO03D) AppleWebKit / 535.19(KHTML, like Gecko) Chrome / 18.0.1025.166 Safari / 535.19",
        "Mozilla / 5.0(Linux;U;Android 4.0.4;en - gb;GT - I9300 Build / IMM76D) AppleWebKit / 534.30(KHTML, like Gecko) Version / 4.0 Mobile Safari / 534.30",
        "Mozilla / 5.0(Linux;U;Android2.2;en - gb;GT - P1000 Build / FROYO) AppleWebKit / 533.1(KHTML, like Gecko) Version / 4.0 Mobile Safari / 533.1"
        "Mozilla / 5.0(Android;Mobile;rv: 14.0) Gecko / 14.0 Firefox / 14.0"
        "Mozilla / 5.0(iPad;CPU OS 5_0 like Mac OS X) AppleWebKit / 534.46(KHTML, like Gecko) Version / 5.1 Mobile / 9 A334 Safari / 7534.48.3"
        "Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3"
    ]
    user_Agent = random.choice(User_Agents)
    # print(user_Agent)
    headers = {
        "User-Agent":user_Agent,
        "Referer":"http://www.mzitu.com/"
    }

    req = requests.get(base_url,headers)
    html = etree.HTML(req.text)
    return html

def mz_spider(base_url):
    html = html_1(base_url)
    # 获取详情页信息
    img_xqy = html.xpath('//div[@class ="postlist"]/ul/li/a/@href')
    for img_url in img_xqy:
        # print(img_url)
        img_parse(img_url)

# 处理详情页
def img_parse(img_url):
    html = html_1(img_url)
    # 获取标题
    title = html.xpath('//div[@class="content"]/h2/text()')[0]
    # print(title)
    # 获取页数
    page_num = html.xpath('//div[@class="pagenavi"]/a/span/text()')[-2]
    # print(page_num)
    # 拼接图片详情页地址
    for num in range(1,int(page_num)+1):
        img_xqy = img_url +'/'+ str(num)
        # print(img_xqy)
        dwon_img(img_xqy,title)

def dwon_img(img_xqy,title):
    User_Agents = [
        "Mozilla / 5.0(Linux;Android 4.1.1;Nexus 7 Build / JRO03D) AppleWebKit / 535.19(KHTML, like Gecko) Chrome / 18.0.1025.166 Safari / 535.19",
        "Mozilla / 5.0(Linux;U;Android 4.0.4;en - gb;GT - I9300 Build / IMM76D) AppleWebKit / 534.30(KHTML, like Gecko) Version / 4.0 Mobile Safari / 534.30",
        "Mozilla / 5.0(Linux;U;Android2.2;en - gb;GT - P1000 Build / FROYO) AppleWebKit / 533.1(KHTML, like Gecko) Version / 4.0 Mobile Safari / 533.1"
        "Mozilla / 5.0(Android;Mobile;rv: 14.0) Gecko / 14.0 Firefox / 14.0"
        "Mozilla / 5.0(iPad;CPU OS 5_0 like Mac OS X) AppleWebKit / 534.46(KHTML, like Gecko) Version / 5.1 Mobile / 9 A334 Safari / 7534.48.3"
        "Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3"
    ]
    user_Agent = random.choice(User_Agents)
    headers = {
        "User-Agent":user_Agent,
        "Referer":"http://www.mzitu.com/"
    }

    html = html_1(img_xqy)

    # 图片具体地址获取
    img_url = html.xpath('//div[@class="main-image"]/p/a/img/@src')[0]
    print(img_url)
    # 下载图片
    title = title.replace(' ','')
    root_dir = 'mz_img' + "/" + title
    img_name = img_url.split('/')[-1]

    print(img_name)
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)
    res = requests.get(img_url,headers)
    with open(root_dir+"/"+img_name,'wb') as f:
        f.write(res.content)
        f.close()
        print(title+"  "+img_name+"文件保存成功")

if __name__ == '__main__':
    for i in range(1,2):
        base_url = "http://www.mzitu.com/826_{}.html".format(str(i))
    mz_spider(base_url)