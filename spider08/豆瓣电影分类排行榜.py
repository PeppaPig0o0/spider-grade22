"""
例 2-10
豆瓣电影分类排行榜
"""
# ① 导入相关库（requests库）
import requests
types = {
    '剧情': '11',
    '喜剧': '24',
    '动作': '5',
    '爱情': '13',
    '科幻': '17',
    '动画': '25'
}
for key, value in types.items():
    print('正在爬取', key, '类型电影')
    for i in range(0, 1000, 20):
        # ② 设置请求URL
        url = 'https://movie.douban.com/j/chart/top_list?type=' + value + '&interval_id=100%3A90&action=&start=' + str(i) + '&limit=20'
        # ③ 定制请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
        }
        # ④ 发起请求，并获取响应
        response = requests.get(url, headers=headers)
        # ⑤ 查看响应结果
        print(response.text)  # 查看响应体
        print('响应状态码', response.status_code)  # 查看响应状态码
        # ⑥ 存储（txt文件中）
        with open('电影.txt', 'a+', encoding='utf-8') as f:
            f.write(response.text)
