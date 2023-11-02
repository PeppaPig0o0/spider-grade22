"""
例：4-2
京东搜索页面爬取，
1.动态加载的数据    网络-XHR
    表头 ——> 请求网址
2.有些网址当中存在%22等特殊符号，因为url编码
    url可以进行解码（更加直观）
3.Cookie
    Cookie存在于客户端，Cookie中包含用户登陆信息
4.Json是一种高度格式化的字符串
    json字符串常用于不同语言、不同程序之间交互数据
    python中有json的标准库
    json.dumps(列表/字典/集合等)   把 列表/字典/集合等类型的数据， 转成json字符串
    json.loads(json字符串)   把json字符串， 转成列表/字典/集合等类型的数据
"""
# ①引入库(requests库,json库)
import requests
import json
# ②设置请求URL
url = 'https://api.m.jd.com/api?functionId=pc_search_adv_Search&appid=search-pc-java&client=pc&clientVersion=1.0.0&uuid=122270672.390870418.1695601868.1695796752.1695803945.5&loginType=3&t=1695804251621&body={"area":"7","enc":"utf-8","keyword":"笔记本","adType":7,"page":"1","ad_ids":"291:33","xtest":"new_search"}&x-api-eid-token=jdd03SN3CYK53IIKPPQWLXCOJWJV2NCGASNOIMECNMDF56Z7YF74GSXGJXGSSDVEWGDT3FPRLDK4S6S3JRSZPMDJOXYHZJMAAAAMK2XG5BLYAAAAAD4PH3UFSVUZLE4X'
# ③定制请求头部(User-Agent，Cookie，Referer)
headers = {
    # 设置UA，伪装成浏览器
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    # 设置Cookie，伪装用户（登陆）信息
    'Cookie': '__jdu=390870418; pinId=QxJfdTC3MWIfeAMlKJarPA; pin=13299001916_p; unick=jd132990uxe; _tp=xrJg1WBja2nYUljFMhAY9g%3D%3D; _pst=13299001916_p; areaId=7; PCSYCityID=CN_410000_410300_0; shshshfpa=fdb43735-6fd9-372a-9187-6181b9693d6c-1654486756; shshshfpx=fdb43735-6fd9-372a-9187-6181b9693d6c-1654486756; ipLoc-djd=7-427-3557-53893; TrackID=13jLpt1XAvglQ2Ld5PC36yQOydgrYBdoL1h21KAeXztBa2sNjHVaA_3iXT1_jCgOWhQhqAoJJRnAfGwTVCje6anjIVQcgKzW1qJu6-_l1aYE; thor=F48F1AF215A9F4CC43E6C9B9E5EA580CC084947416B11D8BB6562C771E76CE293AB517096BBD0F43A8B159662BCC73E478288399D28486D31C117690CF915C52B6C355ECAD6CCEFDE35DCDC7304E3C0B40E59D8A881F21D26BE56FCD90665C7DE5A4FA0E1638D283144095F7019AD71580BDA7E53164463E048D891611380069A3C7BDF8F40E05C56A339EEDDE0656A3; flash=2_d9LAajDlTaJbw3jpgxY37GBfqPnbKAio-3vxQJluuGZ2ayWcXPmhDAASq1LOyeCNY9Mcb-pau54aoA20w_etcEDps2BpM2hUM9v52myrzXM*; ceshi3.com=201; user-key=f4f2e198-351e-4037-b22c-0154272d8dbe; cn=5; unpl=JF8EAK5nNSttXEMBBxIKE0BASFsAW1xaHkQLPWIMBAldGFZXE1ZLExl7XlVdXxRKHx9sYRRUWlNJXA4aBysSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrABMTGU1cUV5UOEonBF9XNVZdXkxSAisDKxMgCQkIV14MQxUEImUNVVReSlEFEjIaIhM; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_59d3899ca27e40cdb9c48ae4b3c9ea08|1695803944816; jsavif=1; 3AB9D23F7A4B3CSS=jdd03SN3CYK53IIKPPQWLXCOJWJV2NCGASNOIMECNMDF56Z7YF74GSXGJXGSSDVEWGDT3FPRLDK4S6S3JRSZPMDJOXYHZJMAAAAMK2XG5BLYAAAAAD4PH3UFSVUZLE4X; _gia_d=1; __jda=122270672.390870418.1695601868.1695796752.1695803945.5; __jdc=122270672; 3AB9D23F7A4B3C9B=SN3CYK53IIKPPQWLXCOJWJV2NCGASNOIMECNMDF56Z7YF74GSXGJXGSSDVEWGDT3FPRLDK4S6S3JRSZPMDJOXYHZJM; __jdb=122270672.3.390870418|5.1695803945; shshshsID=42e309ac03a010d1d1eba430a8d52f27_3_1695804249196; shshshfpb=AAtZYz9WKErQ3NW_ZNyqRh2GBuWk9bBZUSGdWdQAAAAA',
    # Referer解决跨域问题（一般用不上）
    'Referer': 'https://search.jd.com/',
}
# ④发起请求并获取响应（用requests库中的get方法）
response = requests.get(url=url, headers=headers)
# 解决可能存在的编码问题，加上下面这行
response.encoding = response.apparent_encoding
# ⑤打印结果
r = json.loads(response.text)
for i in r['291']:
    print(i)






