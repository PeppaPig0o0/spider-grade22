"""
例 2-1
网易有道翻译，页面爬取
"""

# ① 导入相关库（urllib库中的request模块）
import urllib.request

# ② 设置请求URL
url = 'https://fanyi.youdao.com/indexLLM.html#/'

# ③ 发起请求，并获取响应
response = urllib.request.urlopen(url)

# ④ 查看响应结果
print(response.read().decode('utf-8'))
