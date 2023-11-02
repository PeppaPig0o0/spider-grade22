"""
案例：好听轻音乐网
下载网站的音乐，以MP3格式保存在  《音乐》文件夹中
"""

# ① 引入库
import re
import queue
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
                music_queue.put(item=(title, music_src),
                                block=True,
                                timeout=None)


def download_mp3():
    while music_queue.qsize():
        title, music_src = music_queue.get(block=True, timeout=10)
        # ⑨ 设置每一首音乐的路径，并保存
        path = f'音乐/{title}.mp3'
        with open(path, 'wb') as f:
            # ⑩ 请求音乐数据
            music_response = requests.get(url=music_src, headers=headers)
            f.write(music_response.content)
        print(f'歌曲：{title} {threading.current_thread().name}下载完成')
        # # 延迟1-3
        time.sleep(random.uniform(1, 3))
    print(f'{threading.current_thread().name} 结束')

if __name__ == '__main__':
    # 音乐下载队列 maxsize队列最大长度，不写\小于1为无限
    music_queue = queue.Queue(maxsize=200)
    # ③ 定制请求头(User-Agent  Referer  Cookie)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Referer': 'http://www.htqyy.com/top/hot',
        'Cookie': 'Hm_lvt_74e11efe27096f6ef1745cd53f168168=1697003520; blk=0; isPlay=0; jploop=false; Hm_lpvt_74e11efe27096f6ef1745cd53f168168=1697004943',
    }
    # 获取所有音乐的标题和下载src,并保存
    threading.Thread(target=get_music_src_list, name='孔灿湘').start()
    while music_queue.qsize() < 50:
        print(f'\r当前队列长度{music_queue.qsize()}，孔灿湘正在努力工作中！')
        time.sleep(1)
    print(f'队列长度50，后续开始下载')
    workers = ['陈浩强', '陈剑博', '郭学凡', '李利丹', '李清振',
               '刘梦鸽', '刘悦', '任玄子', '田宇毫', '王鑫']
    for worker in workers:
        threading.Thread(target=download_mp3, name=worker).start()
        time.sleep(1)


