"""
例4-6
京东商品广告爬取
Json是一种高度格式化的字符串
常用于 不用语言、不同程序之间交互数据
python中有json标准库
json.dumps(列表/字典/集合等)   把列表/字典/集合等类型的数据，转为json字符串
json.loads(json字符串)    把json字符串转为 列表/字典/集合等类型的数据
"""
# ①引入库（requests库、json库）
import json
import requests
# ②设置请求URL
# 如果有%22等特殊字段存在，可以进行url解码（也可以不解码）
url = 'https://api.m.jd.com/api?functionId=pc_search_adv_Search&appid=search-pc-java&client=pc&clientVersion=1.0.0&uuid=122270672.390870418.1695601868.1695782264.1695796752.4&loginType=3&t=1695798598326&body={"area":"7","enc":"utf-8","keyword":"大疆","adType":7,"page":"1","ad_ids":"291:33","xtest":"new_search"}&x-api-eid-token=jdd03SN3CYK53IIKPPQWLXCOJWJV2NCGASNOIMECNMDF56Z7YF74GSXGJXGSSDVEWGDT3FPRLDK4S6S3JRSZPMDJOXYHZJMAAAAMK2V34R4QAAAAADD4HVX2VWOXGTEX'
# ③定制请求头
headers = {  # 字典每个键值对（每行），后面必须有逗号
    # 设置UA，伪装成浏览器
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    # 设置Cookie，伪装登陆（用户）信息
    'Cookie': '__jdu=390870418; pinId=QxJfdTC3MWIfeAMlKJarPA; pin=13299001916_p; unick=jd132990uxe; _tp=xrJg1WBja2nYUljFMhAY9g%3D%3D; _pst=13299001916_p; areaId=7; PCSYCityID=CN_410000_410300_0; shshshfpa=fdb43735-6fd9-372a-9187-6181b9693d6c-1654486756; shshshfpx=fdb43735-6fd9-372a-9187-6181b9693d6c-1654486756; ipLoc-djd=7-427-3557-53893; unpl=JF8EAK1nNSttWk1SAU9QG0UWGVVWW10JTR8GbjBRBAhRGVxVTwAaFEV7XlVdXxRKHx9sYRRUWFNJXA4bASsSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrABMTGU1cUV5UOEonBF9XNV1cW01QNRoyGiJSHwFTWFQBSRBObW8EXVtZTlQMKwMrEQ; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_3775ec1f7c934107940fead8c9ae307d|1695796751978; TrackID=13jLpt1XAvglQ2Ld5PC36yQOydgrYBdoL1h21KAeXztBa2sNjHVaA_3iXT1_jCgOWhQhqAoJJRnAfGwTVCje6anjIVQcgKzW1qJu6-_l1aYE; thor=F48F1AF215A9F4CC43E6C9B9E5EA580CC084947416B11D8BB6562C771E76CE293AB517096BBD0F43A8B159662BCC73E478288399D28486D31C117690CF915C52B6C355ECAD6CCEFDE35DCDC7304E3C0B40E59D8A881F21D26BE56FCD90665C7DE5A4FA0E1638D283144095F7019AD71580BDA7E53164463E048D891611380069A3C7BDF8F40E05C56A339EEDDE0656A3; flash=2_d9LAajDlTaJbw3jpgxY37GBfqPnbKAio-3vxQJluuGZ2ayWcXPmhDAASq1LOyeCNY9Mcb-pau54aoA20w_etcEDps2BpM2hUM9v52myrzXM*; ceshi3.com=201; jsavif=1; __jda=122270672.390870418.1695601868.1695782264.1695796752.4; __jdc=122270672; token=612deccbca7bf7e70db5dc1cee9f5461,3,942109; user-key=f4f2e198-351e-4037-b22c-0154272d8dbe; cn=5; 3AB9D23F7A4B3CSS=jdd03SN3CYK53IIKPPQWLXCOJWJV2NCGASNOIMECNMDF56Z7YF74GSXGJXGSSDVEWGDT3FPRLDK4S6S3JRSZPMDJOXYHZJMAAAAMK2V34R4QAAAAADD4HVX2VWOXGTEX; _gia_d=1; 3AB9D23F7A4B3C9B=SN3CYK53IIKPPQWLXCOJWJV2NCGASNOIMECNMDF56Z7YF74GSXGJXGSSDVEWGDT3FPRLDK4S6S3JRSZPMDJOXYHZJM; __jdb=122270672.11.390870418|4.1695796752; shshshsID=f335b14c3ee69a42a122a6ea5081c893_10_1695798596247; shshshfpb=AAvUXedWKErQ3NW_ZNyqRh2GBuWk9bBZUSGdWcgAAAAA',
    # Referer解决可能存在的跨域问题，一般用不上
    'Referer': 'https://search.jd.com/',
}
# ④ 发起请求 获取响应（使用requests库中的get方法请求）
response = requests.get(url=url, headers=headers)
# 解决可能存在的编码问题，加上下面这行
response.encoding = response.apparent_encoding

# ⑤解析
...  # 占位符，Python语法，其他语言没有
r = json.loads(response.text)
# ⑥打印结果
for i in r['291']:
    print(i)







