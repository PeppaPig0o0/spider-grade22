"""
案例：梨视频
采集梨视频人物部分内容
Ajax请求、使用多线程采集
"""
# ① 引入库
import threading
import time
import queue
import requests
from lxml import etree
import re

def worker():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Cookie': 'PEAR_UUID=3ac6579f-9200-4d64-93a3-6f025c32c64a; _uab_collina=170130375118794336987514; Hm_lvt_9707bc8d5f6bba210e7218b8496f076a=1701303753; p_h5_u=44AEEDE8-7CB3-45C1-94F7-061B4EF13FEA; PEAR_UID=CoW13UT9JTeNRZBxCX8EWg==; PEAR_TOKEN=d239e515-7006-4b0b-8bfe-25f9df7cf94f; Hm_lpvt_9707bc8d5f6bba210e7218b8496f076a=1701308158; tgw_l7_route=c94993c99ec065901a2ef1434ac92da5; JSESSIONID=677B336A23D060074D58AE17B3A0F3F7',
        'Referer': 'https://www.pearvideo.com/panorama',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Host': 'www.pearvideo.com',


    }
    url = 'https://www.pearvideo.com/category_loading.jsp'
    for start in range(0, 2000, 24):
        params = {
            'reqType': '5',
            'categoryId': '59',
            'start': start,
        }
        response = requests.get(url, headers=headers, params=params)
        html = etree.HTML(response.text)
        href_list = html.xpath('//div[@class="vervideo-bd"]/a/@href')
        for href in href_list:
            videoid = href.split("_")[1]
            print(videoid)
            href = f'https://www.pearvideo.com/videoStatus.jsp?contId={videoid}'

            headers['Referer'] = f'https://www.pearvideo.com/video_{videoid}'
            r = requests.get(href, headers=headers)
            srcurl = r.json()['videoInfo']['videos']['srcUrl']

            # src = (srcurl.rsplit("/", maxsplit=1)[0]
            #        + '/cont-' + videoid + '-'
            #        + srcurl.rsplit("/", maxsplit=1)[1].split("-", maxsplit=1)[1])
            src = 'https://video.pearvideo.com/mp4/short/20170914/cont-1155543-10883156-hd.mp4'
            h = headers
            h['Referer'] = src
            r = requests.get(src, headers=headers)
            print(r.content)
            with open('a.mp4', 'wb') as f:
                f.write(r.content)
            print('结束')
            time.sleep(1000)
            # src = h.xpath('//video/@src')[0]
            # print(src)


# https://video.pearvideo.com/mp4/third/20220909/1701308707820-11905134-102101-hd.mp4
# https://video.pearvideo.com/mp4/third/20220909/cont-1771041-11905134-102101-hd.mp4
# https://video.pearvideo.com/mp4/short/20170914/cont-1155543-10883156-hd.mp4
if __name__ == '__main__':
    # ② 设置URL
    worker()


