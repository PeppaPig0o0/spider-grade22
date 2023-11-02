"""
例 3-1
爬取三国演义或西游记的目录
"""
# ①引入库（requests库）
import requests
from lxml import etree
# ②设置URL
url = 'https://xiyouji.5000yan.com/'
# ③定制头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}
# ④发起请求，并获取响应
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding  # 修改编码
# ⑤解析页面
html = etree.HTML(response.text)  # 新建一个HTML对象
# 根据xpath路径，解析网页
a_list = html.xpath('/html/body/div[2]/div[1]/main/ul/li/a/text()')
href_list = html.xpath('/html/body/div[2]/div[1]/main/ul/li/a/@href')
# ⑥打印结果
print(a_list)  # 打印章节目录
for i in range(0, len(href_list)):
    # ⑦设置子页面URL
    sublink = href_list[i]  # 下标为i的章节的url
    name = a_list[i]  # 章节名称
    # ⑧对子页面请求并获取响应
    r = requests.get(sublink, headers=headers)
    r.encoding = r.apparent_encoding  # 修改编码
    # ⑨解析子页面
    html = etree.HTML(r.text)  # 新建一个HTML对象
    # 根据xpath路径，解析子页面
    p_list = html.xpath('/html/body/div[2]/div[1]/main/section/div[1]/div/text()')
    path = './西游记/' + name + '.txt'
    with open(path, 'a+', encoding='utf-8') as f:
        f.write('想看更多电子书，请联系洛科孔灿湘！电话：123456789\n认准孔灿湘正版，拒绝盗版李清振\n')
    for p in p_list:
        # ⑩数据清洗，去除不需要的特殊字符
        p = p.replace('\r\n\t', '').replace('\r\n\t\xa0', '').replace(' ', '')
        print(p)
        # 11、存储（按章节存储到txt文件）
        with open(path, 'a+', encoding='utf-8') as f:
            f.write(p + '\n')
