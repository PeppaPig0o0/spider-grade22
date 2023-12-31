"""
例:4-6
京东商品爬取
"""
# ①引入库(requests库)
import requests
import json
# ②设置URL
url = 'https://api.m.jd.com/api?functionId=pc_search_adv_Search&appid=search-pc-java&client=pc&clientVersion=1.0.0&uuid=122270672.390870418.1695601868.1695601869.1695688552.2&loginType=3&t=1695690541118&body={"area":"7","enc":"utf-8","keyword":"华为","adType":7,"page":"1","ad_ids":"291:33","xtest":"new_search"}&x-api-eid-token=jdd03SN3CYK53IIKPPQWLXCOJWJV2NCGASNOIMECNMDF56Z7YF74GSXGJXGSSDVEWGDT3FPRLDK4S6S3JRSZPMDJOXYHZJMAAAAMKZ4CESVIAAAAAD4LHZFLANQ4ADUX'

# ③定制请求头
headers = {
    # UA 伪装成浏览器内核
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeb'
                  'Kit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    # Cookie伪装登陆信息
    'Cookie': '__jdu=390870418; pinId=QxJfdTC3MWIfeAMlKJarPA; pin=13299001916_p; unick=jd132990uxe; _tp=xrJg1WBja2nYUljFMhAY9g%3D%3D; _pst=13299001916_p; areaId=7; PCSYCityID=CN_410000_410300_0; shshshfpa=fdb43735-6fd9-372a-9187-6181b9693d6c-1654486756; shshshfpx=fdb43735-6fd9-372a-9187-6181b9693d6c-1654486756; ipLoc-djd=7-427-3557-53893; unpl=JF8EAK5nNSttD05UAU5QTxEVHFQDWwgAT0RQa2ABUwpeT1EET1UfEBh7XlVdXxRKHx9sYBRVVFNJUw4fAisSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrABMTGU1cUV5UOEonBF9XNVRdX01SAysDKxMgCQkIXV0JSB8KImUNVVReSlEFEjIaIhM; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_f415dce24f8f4d95bb5656f7540ef539|1695688612182; mba_muid=390870418; wlfstk_smdl=ixdap7yqzkkxmzqohpbndfz0plsrtipb; ceshi3.com=201; TrackID=15fd29BAHgMyki-_oS12RiZO6mr2m1l4DMS5WREeXOFSVV_tU1qiElaY0BuqshOJz5OeiFX-Nv7hJshvihuMLYTFzJCvDdzImcU2L38DXtOk; thor=F48F1AF215A9F4CC43E6C9B9E5EA580CC084947416B11D8BB6562C771E76CE29CB6516B23EB8F6534E3128C52E391120069EA26BE6D34B4DA1F15A9551449DB5CD9328D255D7B1A244997C16B967BF76EDEC61ED7A1B216D860F873ED3A410E41AB0133C5D0E9D5C009BD226A1F183DA36F0DCDBC81581EA6A7DB278E1E0BE5C15CBBB836760A49F36AAC55933754317; flash=2_eifHmgKlf7mUc9_4nhH_adgwiE8VNWLK-5p1UXs9TI95F-C6omYz0RLlvEsLtVikFDzbsUU62aYr_pHqjVLYnaotMo4og34qNqHGZLxIAjk*; jsavif=1; TARGET_UNIT=bjcenter; __jda=122270672.390870418.1695601868.1695601869.1695688552.2; __jdc=122270672; token=45b1171de683fe38eb72c802c3884cbe,3,942049; __tk=rUfFKzbW1zM5qurtKz1nqAs52YM3KzSE1YqnqUVB1DxDquSCrwPW2M,3,942049; 3AB9D23F7A4B3CSS=jdd03SN3CYK53IIKPPQWLXCOJWJV2NCGASNOIMECNMDF56Z7YF74GSXGJXGSSDVEWGDT3FPRLDK4S6S3JRSZPMDJOXYHZJMAAAAMKZ4CESVIAAAAAD4LHZFLANQ4ADUX; shshshsID=3a638b34d3bfaf6cfbd7c77cc73d9e4e_22_1695690328504; shshshfpb=AAnkJBc-KErQ3NW_ZNyqRh2GBuWk9bBZUSGdWXgAAAAA; 3AB9D23F7A4B3C9B=SN3CYK53IIKPPQWLXCOJWJV2NCGASNOIMECNMDF56Z7YF74GSXGJXGSSDVEWGDT3FPRLDK4S6S3JRSZPMDJOXYHZJM; joyya=1695689355.1695690504.27.0grillt; __jdb=122270672.25.390870418|2.1695688552',
    # 解决跨域问题
    'Referer': 'https://search.jd.com/',
}
# ④发起请求并获取响应
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
# ⑤解析网页
a = json.loads(response.text)
# ⑥打印结果
for i in a['291']:
    print(i)

