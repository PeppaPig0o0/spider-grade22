import time
# .....
# ①引入库（requests库,lxml库中的etree模块）
import requests
from lxml import etree
# ②设置目录页URL
# url = 'https://pic.netbian.com/e/extend/downpic.php?id=32328&t=0.18027998035286831'
url = 'https://api.zzzmh.cn/bz/v3/download'
data = {
    'id': '8373377e69c3499d904877fab8c6f329'
}
# ③定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Referer':'https://bz.zzzmh.cn/',
'Origin':'https://bz.zzzmh.cn',
'authority':'api.zzzmh.cn',
    'path': '/bz/v3/download',

'Accept':'application/json, text/plain, */*',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Content-Length':'41',
'Content-Type':'application/json;charset=UTF-8',

'Pragma':'no-cache',
'Sec-Ch-Ua':'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
'Sec-Ch-Ua-Mobile':'?0',
'Sec-Ch-Ua-Platform':"Windows",
'Sec-Fetch-Dest':'empty',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'same-site',

   # 'Cookie': 'PHPSESSID=u35p1tbj88hmrm8fk0ja9uvac0; zkhanmlusername=PeppaPig; zkhanmluserid=7220338; zkhanmlgroupid=1; zkhanmlrnd=8TU8uusAPHjtE7G8p6iY; zkhanmlauth=22c11b57ce5369278001daee65c7cfd0'
}
# ④发起请求，并获取相应
response = requests.post(url, headers=headers, data=data)
# response.encoding = response.apparent_encoding
print(response.status_code)
print(response.text)