"""
例 2-1
爬取网易有道翻译页面
"""
# ①引入库（urllib库中的request模块）
import urllib.request

# ②设置URL
url = 'https://fanyi.youdao.com/indexLLM.html#/'

# ③发起请求，并获取响应
response = urllib.request.urlopen(url)

# ④打印结果
print(response.read().decode('utf-8'))
