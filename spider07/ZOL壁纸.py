"""
案例：爬取ZOL壁纸
功能：
爬取ZOL壁纸的笔记本壁纸——>2880×1800分辨率
笔记本壁纸每个分类自动创建一个文件夹，保存壁纸
"""

# ①引入库
import os  # 目录、路径
import time  # 时间模块
import random  # 随机模块
import requests  # 发起http请求
from lxml import etree  # 解析网页
# ②定制请求头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
}
# ③设置请求url
url = 'https://desk.zol.com.cn/nb/'
# ④发起请求并获取响应(requests库中的get方法)
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
# ⑤解析网页
html = etree.HTML(response.text)
type_list = html.xpath('//dl[@class="filter-item first clearfix"]/dd/a')
# ⑥打印结果（索引从1开始，因为第0项是”全部“）
for type in type_list[1:]:
    type_name = type.xpath('text()')[0]  # 解析壁纸分类的名字
    type_href = type.xpath('@href')[0]  # 解析壁纸分类的href（不完整）
    # print(type_name, type_href)

    pic_set_url = f"https://desk.zol.com.cn/{type_href.split('/')[1]}/2880x1800_p4/"
    print(type_name, pic_set_url)








