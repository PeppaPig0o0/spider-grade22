"""
案例：好听轻音乐网   http://www.htqyy.com/
爬取好听轻音乐网站，下载保存音乐mp3 到 《音乐》目录中
"""
# ① 引入库(requests库、lxml库中的etree模块、time库)
import threading
import queue
import re
import time
import requests
from lxml import etree
# ② 设置URL
def put_music_queue() -> None:
    """
    解析页面，获取音乐的标题和src，并插入到队列当中
    return: None
    """
    ranks = ['http://www.htqyy.com/top/musicList/hot',  # 热播榜
             'http://www.htqyy.com/top/musicList/new',  # 新曲榜
             'http://www.htqyy.com/top/musicList/recommend',
             'http://www.htqyy.com/genre/musicList/1',
             'http://www.htqyy.com/genre/musicList/3',
             'http://www.htqyy.com/genre/musicList/5']
    for rank in ranks:
        for page in range(0, 25):
            url = f'{rank}?pageIndex={page}&pageSize=20'

            # ④ 发起请求（使用requests库的get方法）
            response = requests.get(url=url, headers=headers)
            response.encoding = response.apparent_encoding
            # ⑤ 解析页面
            html = etree.HTML(response.text)
            a_list = html.xpath('//ul[@id="musicList"]/li/span[2]/a')
            # ⑥ 打印结果
            for a in a_list:
                title = a.xpath('@title')[0]  # 歌曲名称
                sid = a.xpath('@sid')[0]  # 歌曲编号
                # ⑦ 音乐播放页面地址
                href = 'http://www.htqyy.com/play/' + sid
                # ⑧ 请求音乐播放页
                r = requests.get(url=href, headers=headers)
                r.encoding = r.apparent_encoding
                # ⑨ 子页面解析,获取音乐src
                music_src = 'http://f5.htqyy.com/play9/' + \
                            re.findall(r"\d{1,8}/\w{3}/\d{1,5}", r.text)[0]
                # 向队列中插入一个
                music_queue.put((title, music_src), block=True)


def download_mp3() -> None:
    """
    从队列中取一条数据，根据src下载并保存音乐
    return: None
    """
    while not music_queue.empty():
        item = music_queue.get()
        title, music_src = item[0], item[1]
        # ⑩ 设置路径，下载并保存音乐
        path = f'音乐/{title}.mp3'
        with open(path, 'wb') as f:
            music_response = requests.get(url=music_src, headers=headers)
            f.write(music_response.content)
        print(f'歌曲{title}下载完成，{threading.current_thread().name}')
    print(f'{threading.current_thread().name}线程下班了！')


if __name__ == '__main__':
    print('主函数开始运行')
    # ③ 定制请求头
    headers = {
        # UA伪装成浏览器
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        # 解决跨域问题（一般用不到）
        'Referer': 'http://www.htqyy.com/top/hot',
        # 伪装Cookie，伪装用户登录信息
        'Cookie': 'blk=0; jploop=false; Hm_lvt_74e11efe27096f6ef1745cd53f168168=1697157184,1697611346,1697713079,1697769319; Hm_lpvt_74e11efe27096f6ef1745cd53f168168=1697770230',
    }
    # 设置音乐下载队列
    music_queue = queue.Queue(maxsize=200)
    threading.Thread(target=put_music_queue, name='张程琪').start()
    while music_queue.qsize() < 50:
        print(f'\r当前队列长度{music_queue.qsize()}', end='')
        time.sleep(1)
    print('开始下载')
    workers = ['叶红', '晏祥', '王纤纤', '徐勇梅', '胡省慧', '李婉玉', '李冉', '李勇娜', '周菊']
    for worker in workers:
        t = threading.Thread(target=download_mp3, name=worker)
        t.start()
        print(f'{worker}开始工作')
        time.sleep(1)


