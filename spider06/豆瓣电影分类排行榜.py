"""
例 2-
爬取豆瓣电影分类排行榜
"""
# ①引入库（requests库）
import requests
types = [11, 24, 5, 1, 23, 28, 3]  # 准备电影的类型编号
for j in types:  # 遍历电影的类型
    for i in range(0, 1000, 20):  # 循环采集某个类型的电影
        # ②设置URL
        url = 'https://movie.douban.com/j/chart/top_list?type=' + str(j) + '&interval_id=100%3A90&action=&start=' + str(i) + '&limit=20'
        # ③定制头部
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        }
        # ④发起请求，并获取响应
        response = requests.get(url, headers=headers)
        # ⑤打印结果
        print(response.text)  # 打印响应体的内容
        print(response.status_code)  # 打印响应状态码
        # ⑥存储（txt文件）
        with open('电影.txt', 'a+', encoding='utf-8') as f:
            f.write(response.text)