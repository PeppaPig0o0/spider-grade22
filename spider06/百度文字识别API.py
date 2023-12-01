"""
案例：文字识别
调用百度OCR接口，高精度带位置
"""
import requests
import base64
def get_access_token(APIkey, SecretKey):
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
    return response.json()['access_token']


if __name__ == '__main__':
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate"
    # 二进制方式打开图片文件
    f = open('./3.png', 'rb')
    img = base64.b64encode(f.read())
    params = {"image": img}
    access_token = get_access_token(APIkey='LsXf7qkaFQe5DK12CoWDkbfD',
                                    SecretKey='Tq2Fwtpdr0S6fUa6UouEHElpC9dIWHwW')
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        for i in response.json()['words_result']:
            print(i['words'])
