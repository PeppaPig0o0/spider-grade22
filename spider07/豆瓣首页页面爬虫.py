"""
例 2-7
爬取豆瓣首页页面
"""
# ①引入库（requests库）
import requests
# ②设置url
url = 'https://www.douban.com'
# ③定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
# ④发起请求，并获取响应
response = requests.get(url, headers=headers)
# ⑤打印结果
print(response.text)  # 打印响应内容
print(response.status_code)  # 打印响应状态码
