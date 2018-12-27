import requests
from bs4 import BeautifulSoup
def bl_spider(base_url):
    headers = {
       "User-Agent":"Mozilla / 5.0(Linux;U;Android 4.0.4;en - gb;GT - I9300 Build / IMM76D) AppleWebKit / 534.30(KHTML, like Gecko) Version / 4.0 Mobile Safari / 534.30",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    }

    html = requests.get(base_url)

    soup = BeautifulSoup(html.text,"lxml")

    items = soup.select('div[class="post_item_body"]')

    for item in items:
        # 标题
        title = item.select('h3 a[class="titlelnk"]')[0].get_text()
        print(title)
        # 获取详情页信息
        href = item.select('h3 a[class="titlelnk"]')[0]['href']
        # print(href)
        # 作者
        author = item.select('div a[class="lightblue"]')[0].get_text()
        # 作者主页链接
        author_link = item.select('div a[class="lightblue"]')[0]["href"]
        # print(author_link+"  "+author)
        # 简要信息
        infos = item.select('p[class="post_item_summary"]')[0].get_text().strip('\r\n').strip(' ')
        # print(infos)
        datas = item.select('div[class="post_item_foot"]')[0].get_text()
        # print(datas)
        datas = datas.split(" ")
        # print(datas)
        # ['\n确认沉默', '\r\n', '', '', '', '发布于', '2018-12-24', '09:20', '\r\n', '', '', '', '\r\n', '', '', '', '', '', '',
        # '', '评论(0)阅读(18)']
        # 时间
        time = datas[6]+" "+datas[7]
        # print(time)
        # 评论数
        comment = datas[-1].lstrip('评论(').split(")")[0]
        # print(comment)
        # 阅读量
        read_num = datas[-1].lstrip('评论(').rstrip(')').split('(')[-1]
        # print(read_num)

if __name__ == '__main__':
    # for i in range(1,3):
    #     url = "http://www.cnblogs.com/cate/python/#p{}".format(str(i))
    bl_spider("http://www.cnblogs.com/cate/python/#p3")




