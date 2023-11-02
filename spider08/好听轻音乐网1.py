"""
案例:好听轻音乐网
爬取好听轻音乐网站，保存音乐到 《音乐》目录中
"""
# ① 引入库
import threading
import time
import random
import re
import queue
import requests
from lxml import etree


# ② 设置请求URL
class Downloader(threading.Thread):
    def run(self) -> None:
        while not music_queue.empty():
            item = music_queue.get(block=True, timeout=20)
            title, music_src = item[0], item[1]
            # title = random.choice(list(music_list.keys()))
            # music_src = music_list.pop(title)
            # ⑨ 设置音乐的保存路径
            path = f'音乐/{title}.mp3'
            with open(path, 'wb') as f:
                music_response = requests.get(url=music_src, headers=headers)
                f.write(music_response.content)
            print(f'歌曲{title}下载完成,{threading.current_thread().name}队列长度{music_queue.qsize()}')
            time.sleep(random.randrange(1, 3))
        print(f'{threading.current_thread().name},线程结束！')


class Worker(threading.Thread):
    def run(self) -> None:
        ranks = ['http://www.htqyy.com/top/musicList/hot',
                 'http://www.htqyy.com/top/musicList/new',
                 'http://www.htqyy.com/top/musicList/recommend',
                 'http://www.htqyy.com/genre/musicList/1',
                 'http://www.htqyy.com/genre/musicList/3',
                 'http://www.htqyy.com/genre/musicList/5']
        for rank in ranks:
            for i in range(0, 25):
                url = f'{rank}?pageIndex={i}&pageSize=20'
                print(url)
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
                    link_queue.put((title, href))



class LinkWorker(threading.Thread):
    def run(self) -> None:
        while not link_queue.empty():
            item = link_queue.get(block=True, timeout=20)
            title, href = item[0], item[1]
            # ⑦ 请求子页面
            r = requests.get(url=href, headers=headers)
            r.encoding = r.apparent_encoding
            # ⑧ 子页面解析,获取音乐src
            music_src = 'http://f5.htqyy.com/play9/' + \
                        re.findall(r"\d{1,8}/\w{3}/\d{1,5}", r.text)[0]
            # 建立队列
            # music_list[title] = music_src
            music_queue.put((title, music_src), block=True, timeout=None)
            print(f'当前音乐长度队列长度{music_queue.qsize()}')

if __name__ == '__main__':
    link_queue = queue.Queue(maxsize=200)
    music_queue = queue.Queue(maxsize=200)
    # ③ 定制请求头部(User-Agent、Referer、Cookie)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Referer': 'http://www.htqyy.com/top/hot',
        'Cookie': 'blk=0; jploop=false; jpvolume=0.685; Hm_lvt_74e11efe27096f6ef1745cd53f168168=1698020440,1698106867,1698201366,1698283373; Hm_lpvt_74e11efe27096f6ef1745cd53f168168=1698283381',
    }
    print('好听轻音乐网，开始爬取音乐，请稍等！')

    worker = Worker(name='搬运')
    worker.start()

    linkworker_threads = [LinkWorker() for i in range(5)]
    for t in linkworker_threads:
        t.start()
        print('子页面爬去线程启动')
        time.sleep(1)


    while music_queue.qsize() < 50:
        print(f'\r{music_queue.qsize()}', end='')
        time.sleep(1)
    print('开始下载')

    worker_threads = [Downloader(name=i) for i in
                      ['郑大川', '任移旺', '王高岩', '张震', '熬冬冬', '丁旭', '李宁', '彭震', '姚远洋']]
    for t in worker_threads:
        t.start()
        time.sleep(1)
    # for t in linkworker_threads:
    #     t.join()
    for t in worker_threads:
        t.join()
    music_queue.join()
