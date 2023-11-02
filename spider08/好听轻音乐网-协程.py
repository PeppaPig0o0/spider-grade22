"""
案例:好听轻音乐网
爬取好听轻音乐网站，保存音乐到 《音乐》目录中
"""
# ① 引入库
import threading
import asyncio
import httpx
import time
import random
import re
import requests
from lxml import etree

# ③ 定制请求头部(User-Agent、Referer、Cookie)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Referer': 'http://www.htqyy.com/top/hot',
    'Cookie': 'blk=0; jploop=false; jpvolume=0.685; Hm_lvt_74e11efe27096f6ef1745cd53f168168=1698020440,1698106867,1698201366,1698283373; Hm_lpvt_74e11efe27096f6ef1745cd53f168168=1698283381',
}
_ranks = ['http://www.htqyy.com/top/musicList/hot',
             'http://www.htqyy.com/top/musicList/new',
             'http://www.htqyy.com/top/musicList/recommend',
             'http://www.htqyy.com/genre/musicList/1',
             'http://www.htqyy.com/genre/musicList/3',
             'http://www.htqyy.com/genre/musicList/5']
client = httpx.AsyncClient(headers=headers, verify=False, timeout=None)

# ② 设置请求URL
async def download_mp3():
    await asyncio.sleep(random.randrange(10,20))
    print('开始下载音乐')
    while music_list:
        title = random.choice(list(music_list.keys()))
        music_src = music_list.pop(title)
        path = f'音乐/{title}.mp3'
        with open(path, 'wb') as f:
            music_response = await client.get(url=music_src)
            f.write(music_response.content)
        print(f'歌曲{title}下载完成,{threading.current_thread().name}')
        await asyncio.sleep(random.randrange(1, 3))
    print('下载携程结束')


async def worker(ranks):
    for rank in ranks:
        for i in range(0, 25):
            url = f'{rank}?pageIndex={i}&pageSize=20'
            print(url)
            # ④ 发起请求(requests库中的get方法)
            response = await client.get(url=url)
            # response.encoding = response.apparent_encoding
            # ⑤ 解析网页
            html = etree.HTML(response.text)
            a_list = html.xpath('//li[@class="mItem"]/span[2]/a')
            for a in a_list:
                title = a.xpath('@title')[0].replace('?', '？')
                sid = a.xpath('@sid')[0]
                # ⑥ 构造子页面url
                href = 'http://www.htqyy.com/play/' + sid
                # ⑦ 请求子页面
                r = await client.get(url=href)
                # r.encoding = r.charset_encoding
                # ⑧ 子页面解析,获取音乐src
                music_src = 'http://f5.htqyy.com/play9/' + \
                            re.findall(r"\d{1,8}/\w{3}/\d{1,5}", r.text)[0]
                # 建立队列
                music_list[title] = music_src

async def main():
    tasks = [asyncio.create_task(download_mp3()) for i in range(20)]
    tasks.insert(0, asyncio.create_task(worker(_ranks[0:1])))
    tasks.insert(1, asyncio.create_task(worker(_ranks[1:])))
    print(tasks)
    res = await asyncio.gather(*tasks)


if __name__ == '__main__':
    print('好听轻音乐网，开始爬取音乐，请稍等！')
    music_list = {}
    asyncio.run(main())
    print('全部下载完成')
