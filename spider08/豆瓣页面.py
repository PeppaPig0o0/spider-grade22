"""
例 2-7
豆瓣首页，页面爬取
"""
# ① 导入相关库（requests库）
import requests
# ② 设置请求URL
url = 'https://www.douban.com/'
# ③ 定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
# ④ 发起请求，并获取响应
response = requests.get(url, headers=headers)
# ⑤ 查看响应结果
print(response.text)  # 查看响应体
print('响应状态码', response.status_code)  # 查看响应状态码
