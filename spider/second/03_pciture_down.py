import requests
import os

url ="https://i.meizitu.net/thumbs/2017/09/102473_09a63_200.jpg"
root = "picture"  # 目录
path = root + "/" + url.split("/")[-1]
try:
    if not os.path.exists(root):  # 判断目录是否存在
        os.mkdir(root)
    if not os.path.exists(path): # 判断文件是否存在
        r = requests.get(url)
        with open(path,"wb") as f:
            f.write(r.content)
            print("文件以保存")
    else:
        print("文件已存在")
except Exception as e :
    print(e)