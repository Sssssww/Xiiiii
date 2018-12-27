from urllib import request,parse
import json
def bd_fanyi(content):
    # 请求地址
    url = "https://fanyi.baidu.com/sug"
    # 参数分装
    data = {
        "kw": content
    }
    # 参数分装转码
    data = parse.urlencode(data)
    # 封装请求头部
    headers = {
        "Content-Length":len(data),
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
    }
    # 封装request对象
    req = request.Request(url,headers=headers,data=bytes(data,encoding="utf-8"))
    rst = request.urlopen(req)
    html = rst.read().decode()
    # print(html)
    # 使用json格式化数据
    json_data = json.loads(html)
    print(json_data)
    for item in json_data["data"]:
        print(item["k"]+"   "+item["v"])
if __name__ == '__main__':
    content = input("输入你要翻译的内容：")
    bd_fanyi(content)
