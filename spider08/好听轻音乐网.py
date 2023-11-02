"""
案例:好听轻音乐网
爬取好听轻音乐网站，保存音乐到 《音乐》目录中
"""
# ① 引入库
import threading
import time
import random
import re
import requests
from lxml import etree
# ② 设置请求URL
def get_music_src():
    ranks = ['http://www.htqyy.com/top/musicList/hot',
             'http://www.htqyy.com/top/musicList/new',
             'http://www.htqyy.com/top/musicList/recommend',
             'http://www.htqyy.com/genre/musicList/1',
             'http://www.htqyy.com/genre/musicList/3',
             'http://www.htqyy.com/genre/musicList/5']
    for rank in ranks:
        for i in range(0, 25):
            url = f'{rank}?pageIndex={i}&pageSize=20'

            # ④ 发起请求(requests库中的get方法)
            response = requests.get(url=url, headers=headers)
            response.encoding = response.apparent_encoding
            # ⑤ 解析网页
            html = etree.HTML(response.text)
            a_list = html.xpath('//li[@class="mItem"]/span[2]/a')
            for a in a_list:
                title = a.xpath('@title')[0]
                sid = a.xpath('@sid')[0]
                # ⑥ 构造子页面url
                href = 'http://www.htqyy.com/play/' + sid
                # ⑦ 请求子页面
                r = requests.get(url=href, headers=headers)
                r.encoding = r.apparent_encoding
                # ⑧ 子页面解析,获取音乐src
                music_src = 'http://f5.htqyy.com/play9/' + \
                            re.findall(r"\d{1,8}/\w{3}/\d{1,5}", r.text)[0]
                # 建立队列
                music_list[title] = music_src


def download_music():
    while music_list:
        title = random.choice(list(music_list.keys()))
        music_src = music_list.pop(title)
        # ⑨ 设置音乐的保存路径
        path = f'音乐/{title}.mp3'
        with open(path, 'wb') as f:
            music_response = requests.get(url=music_src, headers=headers)
            f.write(music_response.content)
        print(f'歌曲{title}下载完成,{threading.current_thread().name}')
        time.sleep(random.randrange(1, 3))
    print(f'{threading.current_thread().name},线程结束！')

if __name__ == '__main__':
    # ③ 定制请求头部(User-Agent、Referer、Cookie)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Referer': 'http://www.htqyy.com/top/hot',
        'Cookie': 'blk=0; jploop=false; jpvolume=0.685; Hm_lvt_74e11efe27096f6ef1745cd53f168168=1698020440,1698106867,1698201366,1698283373; Hm_lpvt_74e11efe27096f6ef1745cd53f168168=1698283381',
    }
    print('好听轻音乐网，开始爬取音乐，请稍等！')
    music_list = {}
    threading.Thread(target=get_music_src, name='孙玉松').start()
    while len(music_list) < 50:
        print(f'\r{len(music_list)}', end='')
        time.sleep(1)
    print('开始下载')
    workers = ['郑大川', '任移旺', '王高岩', '张震', '熬冬冬', '丁旭', '李宁', '彭震', '姚远洋']
    threadings = {}
    for worker in workers:
        threadings[worker] = threading.Thread(target=download_music, name=worker)
        threadings[worker].start()
        time.sleep(1)
    for t in threadings:
        t.join()
    print('音乐全部下载完成')
