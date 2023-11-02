"""
例 2-10
豆瓣电影分类排行榜
"""
# ①引入库（requests库）
import requests, time
types = [11, 24, 5, 20, 2, 29]
for j in types:
    for i in range(0, 1000, 20):
        # ②设置URL
        url = 'https://movie.douban.com/j/chart/top_list?type=' + str(j) + '&interval_id=' \
              '100%3A90&action=&start=' + str(i) + '&limit=20'
        # ③定制请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebK'
                          'it/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
        }
        # ④发起请求，并获取相应
        response = requests.get(url, headers=headers)
        # ⑤输出结果
        print('姓名', time.time())  # 打印姓名和当前时间戳
        print(response.text)  # 打印相应体中的内容（页面、数据）
        print(response.status_code)  # 打印响应状态码
        # ⑥存储（txt文件）
        # open(路径, 模式, 编码)   打开或新建一个文件
        # 模式:w写入  r读取  a读写   +追加
        with open('电影.txt', 'a+', encoding='utf-8') as f:
            f.write(response.text)
