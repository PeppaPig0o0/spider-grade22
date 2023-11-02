"""
例 3-1
三国演义（或其他小说）爬虫
"""
# ①引入库（requests库,lxml库中的etree模块）
import requests
from lxml import etree
# ②设置URL
url = 'https://xiyouji.5000yan.com/'
# ③定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
# ④发起请求，并获取相应
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
# ⑤解析网页
html = etree.HTML(response.text)
a_list = html.xpath('/html/body/div[2]/div[1]/main/ul/li/a/text()')
a_href = html.xpath('/html/body/div[2]/div[1]/main/ul/li/a/@href')
# ⑥输出结果
print(a_list)  # 打印章节目录
print(a_href)  # 打印章节链接(子页面URL)

for i in range(0, len(a_href)):
    # ⑦设置子页面URL
    sublink = a_href[i]
    # ⑧对子页面发起请求并获取响应
    r = requests.get(sublink, headers=headers)
    r.encoding = r.apparent_encoding
    # ⑨解析页面
    html = etree.HTML(r.text)
    p_list = html.xpath('/html/body/div[2]/div[1]/main/section/div[1]/div/text()')
    # ⑩存储（按章节txt文件中）
    name = a_list[i]  # 以章节名作为文件名
    path = './西游记/' + name + '.txt'  # 每章保存的路径
    with open(path, 'a+', encoding='utf-8') as f:
        f.write('想看更多电子书，请联系洛科刘仁杰，电话：123456！\n请支持正版刘仁杰，拒绝盗版崔乐乐！\n')
    for p in p_list:
        p = p.replace('\r\n\t\xa0', '').replace('\r\n\t', '')  # 数据清洗
        with open(path, 'a+', encoding='utf-8') as f:
            f.write(p + '\n')
    with open(path, 'a+', encoding='utf-8') as f:
        f.write('想看更多电子书，请联系洛科刘仁杰，电话：123456！\n请支持正版刘仁杰，拒绝盗版崔乐乐！\n')

