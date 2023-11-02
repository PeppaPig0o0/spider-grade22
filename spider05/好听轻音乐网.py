"""
案例：好听轻音乐网
需求：
采集全站音乐，保存mp3格式到 <音乐>文件夹内
"""
# ① 引入库（requests库、lxml库中的etree模块）
import re
import requests
from lxml import etree
# ② 设置URL
ranks = ['http://www.htqyy.com/top/musicList/hot',
         'http://www.htqyy.com/top/musicList/new',
         'http://www.htqyy.com/top/musicList/recommend',
         'http://www.htqyy.com/genre/musicList/1',
         'http://www.htqyy.com/genre/musicList/3',
         'http://www.htqyy.com/genre/musicList/5']
for rank in ranks:
    for page in range(0, 25):
        url = f'{rank}?pageIndex={page}&pageSize=20'
        # ③ 定制请求头(User-Agent、Referer、Cookie)
        headers = {
            # UA伪装成浏览器
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
            # 解决跨域问题（一般遇不到）
            'Referer': 'http://www.htqyy.com/top/hot',
            # Cookie伪装用户信息
            'Cookie': 'blk=0; jploop=false; Hm_lvt_74e11efe27096f6ef1745cd53f168168=1697003520,1697157184; Hm_lpvt_74e11efe27096f6ef1745cd53f168168=1697157692',
        }
        # ④ 发起请求，并获取响应
        response = requests.get(url=url, headers=headers)
        response.encoding = response.apparent_encoding
        # ⑤ 解析
        html = etree.HTML(response.text)
        a_list = html.xpath('//li[@class="mItem"]/span[2]/a')

        for a in a_list:
            title = a.xpath('@title')[0]
            sid = a.xpath('@sid')[0]
            # ⑥ 设置音乐页面链接
            href = 'http://www.htqyy.com/play/' + sid
            # ⑦ 向音乐页面发起请求，并获取响应
            r = requests.get(url=href, headers=headers)
            r.encoding = r.apparent_encoding
            # ⑧ 子页面解析,获取音乐src
            music_src = 'http://f5.htqyy.com/play9/' + \
                        re.findall(r"\d{1,8}/\w{3}/\d{1,5}", r.text)[0]
            # ⑨ 下载并保存音乐Mp3
            path = f'音乐/{title}.mp3'
            with open(path, 'wb') as f:
                # ⑩ 请求音乐地址
                music_stream = requests.get(url=music_src, headers=headers)
                f.write(music_stream.content)
            print(f'歌曲：{title}。下载完成,路径：{path}')


