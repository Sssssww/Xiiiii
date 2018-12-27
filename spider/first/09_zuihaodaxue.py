from urllib import request
from lxml import etree

base_url = "http://zuihaodaxue.com/zuihaodaxuepaiming2018.html"

rsp = request.urlopen(base_url)
html = rsp.read().decode()
# print(html)

html = etree.HTML(html)

items = html.xpath('//tr[@class="alt"]')
# print(items)

for item in items:
    # 排名
    number = item.xpath('./td')[0].text
    # 学校
    school = item.xpath('.//div[@align="left"]')[0].text
    # 省份
    addr = item.xpath('./td')[2].text
    # 总分
    score = item.xpath('./td')[3].text
    print(number+"    "+school+"    "+addr+"    "+score)