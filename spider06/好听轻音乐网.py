"""
案例：好听轻音乐网
下载网站的音乐，以MP3格式保存在  《音乐》文件夹中
"""

# ① 引入库
import re
import random
import time
import threading
import requests  # 发起http请求
from lxml import etree  # 解析网页


def get_music_src_list():
    # ② 设置url
    ranks = ['http://www.htqyy.com/top/musicList/hot',
             'http://www.htqyy.com/top/musicList/new',
             'http://www.htqyy.com/top/musicList/recommend',
             'http://www.htqyy.com/genre/musicList/1',
             'http://www.htqyy.com/genre/musicList/3',
             'http://www.htqyy.com/genre/musicList/5']
    for rank in ranks:
        for page in range(0, 25):
            url = f'{rank}?pageIndex={page}&pageSize=20'

            # ④ 发起请求并获取响应
            response = requests.get(url=url, headers=headers)
            response.encoding = response.apparent_encoding
            # ⑤ 解析页面
            html = etree.HTML(response.text)
            a_list = html.xpath('//li[@class="mItem"]/span[2]/a')
            for a in a_list:
                title = a.xpath('@title')[0]
                sid = a.xpath('@sid')[0]
                # ⑥ 设置二级页面url
                s_url = 'http://www.htqyy.com/play/' + sid
                # ⑦ 请求二级页面
                r = requests.get(url=s_url, headers=headers)
                r.encoding = r.apparent_encoding
                # ⑧ 解析二级页面,获取音乐src地址
                music_src = 'http://f5.htqyy.com/play9/' + \
                            re.findall(pattern=r"\d{1,8}/\w{3}/\d{1,8}", string=r.text)[0]
                # 建立队列
                music_src_list[title] = music_src


def download_mp3():
    while music_src_list:
        key = random.choice(list(music_src_list.keys()))
        music_src = music_src_list.pop(key)
        # ⑨ 设置每一首音乐的路径，并保存
        path = f'音乐/{key}.mp3'
        with open(path, 'wb') as f:
            # ⑩ 请求音乐数据
            music_response = requests.get(url=music_src, headers=headers)
            f.write(music_response.content)
        print(f'歌曲：{key} {threading.current_thread().name}下载完成')
        # # 延迟1-3
        time.sleep(random.uniform(1, 3))
    print(f'{threading.current_thread().name} 结束')

if __name__ == '__main__':
    # ③ 定制请求头(User-Agent  Referer  Cookie)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Referer': 'http://www.htqyy.com/top/hot',
        'Cookie': 'Hm_lvt_74e11efe27096f6ef1745cd53f168168=1697003520; blk=0; isPlay=0; jploop=false; Hm_lpvt_74e11efe27096f6ef1745cd53f168168=1697004943',
    }
    music_src_list = {}
    # get_music_src_list()
    # 获取所有音乐的标题和下载src,并保存
    threading.Thread(target=get_music_src_list).start()
    time.sleep(5)
    for i in range(20):
        threading.Thread(target=download_mp3, name=f'进程{i}').start()
        time.sleep(1)


