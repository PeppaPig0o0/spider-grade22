"""
案例:好听轻音乐网
爬取好听轻音乐网站，保存音乐到 《音乐》目录中
"""
# ① 引入库
import re
import requests
from lxml import etree
# ② 设置请求URL
url = 'https://www.dianping.com/search/keyword/1222/10_%E6%B4%9B%E9%98%B3/o3'
# ③ 定制请求头部(User-Agent、Referer、Cookie)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Referer': 'https://www.dianping.com/search/keyword/1222/10_%E6%B4%9B%E9%98%B3',
    'Cookie': 'navCtgScroll=0; fspop=test; cy=1222; cye=xinan; _lxsdk_cuid=18b270c239fc8-083d1138286b3-26031e51-144000-18b270c23a0c8; _lxsdk=18b270c239fc8-083d1138286b3-26031e51-144000-18b270c23a0c8; _hc.v=6c99eec1-3c89-fdc9-1d90-10ca26e12cb8.1697167189; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1697167190; s_ViewType=10; WEBDFPID=zyy5z869vu3w5u7zzzv96ww9x1u9931681y729x3w949795880701432-2012527207446-1697167207446AWEUOGQfd79fef3d01d5e9aadc18ccd4d0c95072763; qruuid=db93ffde-019d-485a-863f-f5875b760826; dplet=65fe8472ec7610902399405d30307fd8; dper=d7ddaf7788999a5967b463c5a3b8ee6a4f5487d5690faf33ba843c2abf3681c762336e837e5098d27edca2656ab527f2001ebad2bb01444a434a364e30f11777; ll=7fd06e815b796be3df069dec7836c3df; ua=%E6%B1%A4%E5%9C%B0; ctu=5af460e9d34de480fdf2b9712bc9e17fcecb43899b1c1b401aceb770ac6f9e6f; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1697167511; _lxsdk_s=18b270c23a0-a2a-9eb-de7%7C%7C234',
}
# ④ 发起请求(requests库中的get方法)
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
print(response.status_code)
print(response.text)
# ⑤ 解析网页
# html = etree.HTML(response.text)
# a_list = html.xpath('//li[@class="mItem"]/span[2]/a')
#                   '//*[@id="musicList"]/li/span[2]/a'