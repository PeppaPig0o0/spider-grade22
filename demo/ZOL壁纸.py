import os
import random
import time
import requests
from lxml import etree


# 函数，根据壁纸类型，建立文件夹
def mk_dir(name):
    """新建一个文件夹
    参数 name: 壁纸类型名字
    返回值 无
    """
    path = './笔记本壁纸/' + name + '/'
    if os.path.exists(path):
        
        return 0
    os.mkdir(path)
    
def save_pic(src, path, Referer):
    """下载并保存一张图片
    参数 src: 图片在网络上的地址
    参数 path: 图片保存在本地的路径
    返回值 无
    """
    with open(path, 'wb') as f:
        image = request_and_parse(url=src, Referer=Referer)
        f.write(image.content)
        print('下载成功' + path)

def request_and_parse(url, **kwargs):
    """请求地址，获取响应结果，并根据xpath路径解析
        参数 url: 地址
        参数 xpath: xpath路径
        返回值 解析结果
    """
    headers['Referer'] = kwargs.get('Referer', '')
    response = requests.get(url=url, headers=headers)
    if kwargs.get('xpath'):
        response.encoding = response.apparent_encoding
        html = etree.HTML(response.text)
        return html.xpath(kwargs['xpath'])
    return response

if __name__ == '__main__':
    url = 'https://desk.zol.com.cn/nb/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }

    type_list = request_and_parse(url=url,
                               xpath='//dl[@class="filter-item first clearfix"]/dd/a')

    for type in type_list[1:]:
        wallpaper_type = type.xpath('text()')[0]
        mk_dir(wallpaper_type)

        wallpaper_type_href = f"https://desk.zol.com.cn/{type.xpath('@href')[0].split('/')[1]}/2880x1800_p4/"
        set_href_list = request_and_parse(url=wallpaper_type_href,
                                          xpath='//ul[@class="pic-list2  clearfix"]/li/a/@href')
        for href in set_href_list[2:5]:
            pic_a_list = request_and_parse(url='https://desk.zol.com.cn' + href,
                                          xpath='//ul[@id="showImg"]/li/a')

            for pic_a in pic_a_list:
                pic_number = pic_a.xpath('@href')[0].split('_')[1]
                Referer = f'https://desk.zol.com.cn/showpic/2880x1800_{pic_number}_{str(random.randint(111, 999))}.html'

                try:
                    pic_src = pic_a.xpath('img/@src')[0]
                except IndexError:
                    pic_src = pic_a.xpath('img/@srcs')[0]
                pic_src = pic_src.replace('t_s144x90', 't_s2880x1800')
                image_path = f'./笔记本壁纸/{wallpaper_type}/{str(int(time.time()))}{str(random.randint(111,999))}.jpg'
                save_pic(src=pic_src, path=image_path, Referer=Referer)




