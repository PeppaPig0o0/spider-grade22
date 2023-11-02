"""
例 3-1
爬取三国演义（或其他小说）
"""
# ①导入库（requests库，lxml库中的etree模块）
import requests
from lxml import etree
# ②设置urle
url = 'https://sanguo.5000yan.com/'
# ③定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
# ④发起请求并获取响应
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding  # 调整编码
# ⑤解析页面
html = etree.HTML(response.text)
a_list = html.xpath('/html/body/div[2]/div[1]/main/ul/li/a/text()')
a_href = html.xpath('/html/body/div[2]/div[1]/main/ul/li/a/@href')
# ⑥打印结果
print(a_list)
print(a_href)

for i in range(0, len(a_href)):
    # ⑦设置子页面URL
    sublink = a_href[i]
    # ⑧请求子页面并获取响应
    r = requests.get(sublink, headers=headers)
    r.encoding = r.apparent_encoding  # 调整编码
    # ⑨解析子页面
    html = etree.HTML(r.text)
    p_list = html.xpath('/html/body/div[2]/div[1]/main/section/div[1]/div/text()')
    # ⑩存储(按章节存txt文件中)
    name = a_list[i]
    path = './三国演义/' + name + '.txt'
    for p in p_list:
        p = p.replace('\r\n\t\xa0', '').replace('\r\n\t', '')  # 数据清洗
        print(p)
        with open(path, 'a+', encoding='utf-8') as f:
            f.write(p+'\n')
