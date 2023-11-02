"""
例3-6
爬取Q房网新房信息
"""
# ①引入库（requests库,lxml库中的etree模块,csv库）
import csv
import requests
from lxml import etree
# ②定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Cookie': 'language=SIMPLIFIED; _ga=GA1.1.715371624.1695256394; sid=e99e5665-b243-42c9-88bc-cb49d68d66cc; qchatid=af078f7f-d58a-4fb1-b85f-6bce4da0a575; fuid=e92600bb-fd65-4f08-a51e-87854485c340; userId=14093389; userName=Q%E6%88%BF%E7%94%A8%E6%88%B7; accountId=64d11c64-7474-4381-9b0e-3ed808f72b15; loginphone=13299001916; city=SHENZHEN; pictureUrl=; token=QFANG-eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNDA5MzM4OSIsInN1YiI6IntcImFjY291bnRJZFwiOlwiNjRkMTFjNjQtNzQ3NC00MzgxLTliMGUtM2VkODA4ZjcyYjE1XCIsXCJjaXR5XCI6XCJTSEVOWkhFTlwiLFwiZnVpZFwiOlwiZTkyNjAwYmItZmQ2NS00ZjA4LWE1MWUtODc4NTQ0ODVjMzQwXCIsXCJuYW1lXCI6XCJR5oi_55So5oi3XCIsXCJwaG9uZVwiOlwiMTMyOTkwMDE5MTZcIixcInVzZXJJZFwiOjE0MDkzMzg5fSIsImlhdCI6MTY5NTI1NzMxNiwiaXNzIjoicWZhbmciLCJleHAiOjE2OTU4NjEzMTZ9.Q7gBcBpUbknzTE8sScfb_XhSVaP9Xb88Wz8Dy3VgH9MTqfy4KnaJ24T-qsnBC2bYWJM9lYjZqN58FSWBCj11_Q; _ga_GV01F4QGNH=GS1.1.1695256394.1.1.1695257316.0.0.0; Hm_lvt_ca292e4806dd6e0201252ffc265b65ac=1695257370; CITY_NAME=GUANGZHOU; JSESSIONID=aaaAM9CYY3krq4rQ6uBOy; Hm_lpvt_ca292e4806dd6e0201252ffc265b65ac=1695257380'
}
# ③设置URL
url = 'https://guangzhou.qfang.com/newhouse/list'
# ④ 发起请求，并获取响应
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
# ⑤打印
print(response.text)


