"""
例 3-
爬取飞卢小说网免费小说
"""
# ①导入库（requests库，lxml库中的etree模块）
import requests
from lxml import etree
import os
# ③定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
for page in range(1, 14000):
    # 书库页的URL
    url = 'https://b.faloo.com/y_0_0_0_0_6_1_' + str(page) +'.html'
    # ④发起请求并获取响应
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding  # 调整编码
    # ⑤解析页面
    html = etree.HTML(response.text)
    book_list = html.xpath('/html/body/div[2]/div[3]/div/div/div[1]/div[2]/div[1]/div[1]/h1/a/text()')  # 书的标题
    book_href = html.xpath('/html/body/div[2]/div[3]/div/div/div[1]/div[2]/div[1]/div[1]/h1/a/@href')  # 书的目录链接
    # # ⑥打印结果
    # print(book_list)
    # print(book_href)

    # 所有书的目录页URL
    for j in range(0, len(book_href)):
        # ②设置一本书目录页URL
        url = 'https:' + book_href[j]
        dir_path = './飞卢小说网/'+book_list[j]
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        # url = 'https://b.faloo.com/1354738.html'

        # ④发起请求并获取响应
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding  # 调整编码
        # ⑤解析页面
        html = etree.HTML(response.text)
        a_list = html.xpath('//div[@class="DivTd3"]/a/text()')  # 目录标题
        a_href = html.xpath('//div[@class="DivTd3"]/a/@href')  # 目录链接
        # ⑥打印结果
        # print(a_list)
        print('开始爬取', book_list[j])

        for i in range(0, len(a_href)):
            # ⑦设置子页面URL
            sublink = 'https:' + a_href[i]
            # ⑧请求子页面并获取响应
            r = requests.get(sublink, headers=headers)
            r.encoding = r.apparent_encoding  # 调整编码
            # ⑨解析子页面
            html = etree.HTML(r.text)
            p_list = html.xpath('//div[contains(@class,"noveContent")]/p/text()')
            # ⑩存储(按章节存txt文件中)
            name = a_list[i].replace('?', '？')
            path = dir_path + '/' + name + '.txt'

            for p in p_list:
                p = p.replace('\r\n\t\xa0', '').replace('\r\n\t', '')  # 数据清洗
                # print(p)
                with open(path, 'a+', encoding='utf-8') as f:
                    f.write(p+'\n')



