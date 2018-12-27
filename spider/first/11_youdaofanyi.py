"""
salt: i
i = "" + (new Date).getTime() + parseInt(10 * Math.random(), 10)

sign: n.md5("fanyideskweb" + e + i + "p09@Bn{h02_BIEe]$P^nG")

Cookie:OUTFOX_SEARCH_USER_ID=611097654@10.169.0.84; JSESSIONID=aaa2sQzXlZdKI_UMlhkFw; OUTFOX_SEARCH_USER_ID_NCOO=403355603.6907034; ___rl__test__cookies=1545285370173
"""

import time
import random
from urllib import request,parse
import json
import hashlib  # 用于Md5加密

def getMd5(value):
    md5 = hashlib.md5()
    md5.update(bytes(value,encoding="utf-8"))
    sign = md5.hexdigest()
    return sign

def yd_fayi(key):
    # Request URL:http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
    # 此url 需要去掉里面的_o猜可以使用否则会出现{"errorCode":50}
    base_url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    r = int(time.time()*1000)
    t = r + random.randint(1, 10)
    ts = r
    new_sign = "fanyideskweb" + key + str(t) + "p09@Bn{h02_BIEe]$P^nG"
    data = {
        "i":key,
        'from':'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': t,
        'sign': getMd5(new_sign),
        'ts': ts,
        'bv': 'b8d026a0af60f03f29c5b4cc06dd949d',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false',
    }
    data = parse.urlencode(data)
    headers = {
        'Accept':'application / json, text / javascript, * / *; q = 0.01',
        'Accept - Language': 'zh - CN, zh;q = 0.9',
        'Connection': 'keep - alive',
        'Content - Length': '',
        'Content - Type': 'application / x - www - form - urlencoded;charset = UTF - 8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID = 611097654 @ 10.169.0.84;JSESSIONID = aaa2sQzXlZdKI_UMlhkFw;OUTFOX_SEARCH_USER_ID_NCOO = 403355603.6907034;___rl__test__cookies = 1545285370173',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http: // fanyi.youdao.com',
        'Referer': 'http: // fanyi.youdao.com /User - Agent: Mozilla / 5.0(X11;Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 64.0.3282.119 Safari / 537.36',
        'X - Requested - With': 'XMLHttpRequest'
    }
    req = request.Request(url= base_url,data=bytes(data,encoding="utf-8"),headers=headers)
    rsp = request.urlopen(req)
    content = rsp.read().decode()
    print(content)
    p = eval(content[95:-4])  # content 原本为字符串格式 用eval函数将其转换为字典格式
    print(p["src"],"   ",p["tgt"])

if __name__ == '__main__':
    while True:
        key = input("请输入要翻译的内容(输入q退出):")
        if key == "q":
            break
        yd_fayi(key)