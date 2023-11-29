"""
案例：百度文字识别API
调用百度智能云 通用OCR(高精度位置版)
"""
import time

# encoding:utf-8

import requests
import base64
import json
import tkinter as tk
from tkinter import filedialog
def select_files():
    # files_path = filedialog.askopenfilename()
    files_path = filedialog.askopenfilenames()

window = tk.Tk()
select_button = tk.Button(window, text='选择文件', command=select_files)
select_button.pack()
window.mainloop()
time.sleep(1000)

'''
通用文字识别（高精度含位置版）
'''
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
    response = requests.post(url=url, params=params, headers=headers)
    return json.loads(response.text)['access_token']


if __name__ == '__main__':
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate"
    # 二进制方式打开图片文件
    f = open('图片.png', 'rb')
    img = base64.b64encode(f.read())
    params = {"image": img}

    APIKey = 'APIKey'
    SecretKey = 'SecretKey'
    access_token = get_access_token(APIKey, SecretKey)
    request_url = request_url + "?access_token=" + access_token

    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        for i in json.loads(response.text)['words_result']:
            print(i['words'])
