"""
案例：百度文字识别API
高精度带位置版
"""


# encoding:utf-8
# 引入库
import requests
import base64
import json

'''
通用文字识别（高精度含位置版）
'''
def get_access_token(APIkey, SecretKey):
    """
    百度鉴权接口
    param: APIkey 百度应用APIKey
    param: SecretKey 百度应用SecretKey
    return: access_token
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {
        'client_id': APIkey,  # API Key
        'grant_type': 'client_credentials',
        'client_secret': SecretKey  # Secret Key
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post(url, params=params, headers=headers)
    return json.loads(response.text)['access_token']


if __name__ == '__main__':
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate"
    # 二进制方式打开图片文件
    f = open('./1.png', 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img,
                'paragraph': 'true'
                }
    access_token = get_access_token(APIkey='bk6z2931w0GeOx5ZNiXqbFWD',
                                    SecretKey='c30QHrdAChN8y4iFnhSdp1DjtDe5nqXi')
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        for i in response.json()['words_result']:
            print(i['words'])
