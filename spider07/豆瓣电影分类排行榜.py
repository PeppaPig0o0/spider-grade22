"""
例 2-
爬取豆瓣电影分类排行榜
"""
# ①引入库（requests库）
import requests
types = [11, 24, 20, 7, 4, 3, 16]
for j in types:
    for i in range(0, 1000, 20):
        # ②设置url  剧情
        url = 'https://movie.douban.com/j/chart/top_list?type=' + str(j) + '&int' \
              'erval_id=100%3A90&action=&start=' + str(i) + '&limit=20'
        # ③定制请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
        }
        # ④发起请求，并获取响应
        response = requests.get(url, headers=headers)
        # ⑤打印结果
        print(response.text)  # 打印响应内容
        print(response.status_code)  # 打印响应状态码
        # ⑥存储(txt文件)
        # open(路径, 模式, 编码)  根据路径打开或新建一个文件
        # 模式:w写入  r读取  a读写  +追加   不带+表示覆盖源文件
        with open('电影.txt', 'a+', encoding='utf-8') as f:
            f.write(response.text)



dbcl2="161322257:ufROgLUitzw";
path=/;
domain=.douban.com;
expires=Sun, 08-Oct-2023 03:36:11 GMT;
httponly
