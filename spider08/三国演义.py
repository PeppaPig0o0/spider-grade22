"""
例 3-1
爬取三国演义（或其他小说）
"""
# ① 导入相关库（requests库,lxml库中的etree模块）
import requests
from lxml import etree
# ② 设置请求URL
url = 'https://sanguo.5000yan.com/'
# ③ 定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
# ④ 发起请求，并获取响应
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
# ⑤ 解析网页
html = etree.HTML(response.text)
a_list = html.xpath('/html/body/div[2]/div[1]/main/ul/li/a/text()')
a_href = html.xpath('/html/body/div[2]/div[1]/main/ul/li/a/@href')
# ⑥ 查看响应结果
print(a_list)  # 打印章节目录
print(a_href)  # 打印章节链接
print('响应状态码', response.status_code)  # 查看响应状态码

for i in range(0, len(a_href)):
    # ⑦ 请求子页面链接，并获取响应
    r = requests.get(a_href[i], headers=headers)
    r.encoding = r.apparent_encoding
    # ⑧ 解析子页面
    h = etree.HTML(r.text)
    content_list = h.xpath('/html/body/div[2]/div[1]/main/section/div[1]/div/text()')
    # ⑨ 打印并存储子页面中内容
    print(content_list)
    path = './三国演义/' + a_list[i] + '.txt'  # 每章保存的路径
    with open(path, 'a+', encoding='utf-8') as f:  # 每个txt文件开头加一段话
        f.write('想要购买更多电子书，请联系王高岩，电话：666666\n价格优惠，量大从优！' + '\n')
    for p in content_list:
        p = p.replace('\r\n\t\xa0', '').replace('\r\n\t', '')
        print(p)
        # ⑩存储(存储一个段落)
        with open(path, 'a+', encoding='utf-8') as f:
            f.write(p+'\n')


