"""
例 2-7
豆瓣首页页面爬取
"""
# ①引入库（requests库）
import requests,time
# ②设置URL
url = 'https://www.douban.com'
# ③定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebK'
                  'it/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
# ③发起请求，并获取相应
response = requests.get(url, headers=headers)
# ④输出结果
print('姓名', time.time())  # 打印姓名和当前时间戳
print(response.text)  # 打印相应体中的内容（页面、数据）
print(response.status_code)  # 打印响应状态码