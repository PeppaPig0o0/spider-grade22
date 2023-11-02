"""
例4-6
京东商品广告信息爬取
json 是一种高度格式化的 字符串
通常作为一种数据结构，用于不同编程语言、不同程序之间传递数据
python中有json标准库
json.dumps(列表/字典/集合等)   把列表/字典/集合等转义成json字符串
json.loads(json字符串)    把json字符串 转义为列表/字典/集合等
"""
# ①引入库（requests库，json库）
import json
import requests
# ②设置请求URL
# 如果有%22等存在于url中，是url编码，可以进行解码
url = 'https://api.m.jd.com/api?functionId=pc_search_adv_Search&appid=search-pc-java&client=pc&clientVersion=1.0.0&uuid=122270672.390870418.1695601868.1695688552.1695782264.3&loginType=3&t=1695782737105&body={"area":"7","enc":"utf-8","keyword":"笔记本电脑","adType":7,"page":"1","ad_ids":"291:33","xtest":"new_search"}&x-api-eid-token=jdd03SN3CYK53IIKPPQWLXCOJWJV2NCGASNOIMECNMDF56Z7YF74GSXGJXGSSDVEWGDT3FPRLDK4S6S3JRSZPMDJOXYHZJMAAAAMK2SDQVCIAAAAACVPOSMS6KXKEUMX'
# ③定制请求头
headers = {  # 不要忘了每行后免的逗号！！
    # UA伪装，伪装成浏览器
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    # Cookie，伪装登陆（用户）信息   拿别人的Cookie也可以用
    'Cookie': '__jdu=390870418; pinId=QxJfdTC3MWIfeAMlKJarPA; pin=13299001916_p; unick=jd132990uxe; _tp=xrJg1WBja2nYUljFMhAY9g%3D%3D; _pst=13299001916_p; areaId=7; PCSYCityID=CN_410000_410300_0; shshshfpa=fdb43735-6fd9-372a-9187-6181b9693d6c-1654486756; shshshfpx=fdb43735-6fd9-372a-9187-6181b9693d6c-1654486756; ipLoc-djd=7-427-3557-53893; unpl=JF8EAK5nNSttC0JUUhgFExcRQ1RUWwgPSUQFOjcFAwkMT1JQGwUbRRV7XlVdXxRKHx9sYRRUXFNJUg4ZCysSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrABMTGU1cUV5UOEonBF9XNVxUXU1TDSsDKxMgCQkIWV4NThIGImUNVVReSlEFEjIaIhM; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_b81f269409814d63b7da1fee57d161f4|1695782264157; jsavif=1; __jda=122270672.390870418.1695601868.1695688552.1695782264.3; __jdc=122270672; mba_muid=390870418; wlfstk_smdl=kmbcmkssc9ztg6642ydl3fry3ajwhoy2; TrackID=1fw72pvND-cpBGua3tJtmRB6OsBwJboTd-qQ7rSS_NZRibQuQ6xAqUQC0mxmLeMOEtp-kcSrk1l_Nf6R8ga4x66AWOyd2ldEb7ga79vizfzs; thor=F48F1AF215A9F4CC43E6C9B9E5EA580CC084947416B11D8BB6562C771E76CE2942438628D599E580FCA0567871E19B6C8557726DAEA48F39ED757E4EF5674B82F00E4EA8E334FADFE8ADD0AC8ABE8BD5F64FEB726972A4A9C0522E20924E6ACD7E52D0D359A59F9E958DDEA3EAEBA99EFE3454D6A5F7A2B1F135990C26CEDE53D8436E208A7A67B97A2F46EE759F09A9; flash=2_6dBz1fzhQao4M7KrCpha2jvc5Sj6rv0cUxTxd6XmwAB5P8MUmRPCA4xMJW4oV855XVbyHk9POaPNBIT4VozbqGT0xv_5h740xYY-UFvB6oh*; ceshi3.com=201; 3AB9D23F7A4B3C9B=SN3CYK53IIKPPQWLXCOJWJV2NCGASNOIMECNMDF56Z7YF74GSXGJXGSSDVEWGDT3FPRLDK4S6S3JRSZPMDJOXYHZJM; 3AB9D23F7A4B3CSS=jdd03SN3CYK53IIKPPQWLXCOJWJV2NCGASNOIMECNMDF56Z7YF74GSXGJXGSSDVEWGDT3FPRLDK4S6S3JRSZPMDJOXYHZJMAAAAMK2SDQVCIAAAAACVPOSMS6KXKEUMX; _gia_d=1; __jdb=122270672.12.390870418|3.1695782264; shshshsID=e3ea19b5dee679519a8c16beb9daa4cb_9_1695782735276; shshshfpb=AAlUSh9SKErQ3NW_ZNyqRh2GBuWk9bBZUSGdWaAAAAAA',
    # Referer，解决跨域问题（大部分情况下用不到）
    'Referer': 'https://search.jd.com/',
}
# ④发起请求，并获取响应(用requests库中的get方法，发起请求)
response = requests.get(url=url, headers=headers)
# 为了解决可能存在的编码问题,可以加上这一行
response.encoding = response.apparent_encoding
# ⑤解析数据(把json字符串，转为字典)
...  # 三个点，Python语法 占位符
r = json.loads(response.text)
# ⑥打印结果
for i in r['291']:
    print(i)


