from urllib import request
import  ssl

# ssl 免认证
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://www.csls.cdb.com.cn"
req = request.urlopen(url)
html = req.read().decode("gbk")

print(html)