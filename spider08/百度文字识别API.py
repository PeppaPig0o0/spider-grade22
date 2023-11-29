import time

# encoding:utf-8

import requests
import base64
import requests
import json
import tkinter as tk
from tkinter import filedialog
from PIL import Image
ALLOW_IMG_FORMAT = ['jpg', 'jpeg', 'png', 'bmp']
MAX_SIZE = 111111
MAX_PIX = 8192


def imgs():
    root = tk.Tk()
    root.withdraw()
    files_path = filedialog.askopenfilenames()  # 获取文件夹中的某文件
    for file_path in files_path:
        # 打开图片
        image = Image.open(file_path)
        width, height = image.size
        if width > 4096 or height > 4096:
            per = 4096/width if width > height else 4096/height
            image = image.resize((int(width*per-1), int(height*per-1)), Image.LANCZOS)

        image.save(file_path)
        with open(file_path, 'rb') as f:
            yield base64.b64encode(f.read()), file_path


def get_access_token(APIkey, SecretKey):
    url = "https://aip.baidubce.com/oauth/2.0/token"
    # url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=EW6uYdn6HOaptoopSvMhjyHb&client_secret=9OhjiLybW5yuYfWbGjEErXqSU8EOXdmc"
    params = {
        'client_id': APIkey,  # API Key
        'grant_type': 'client_credentials',
        'client_secret': SecretKey  # Secret Key
    }
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, params=params, headers=headers, data=payload)
    access_token = json.loads(response.text)['access_token']
    return access_token


if __name__ == '__main__':
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate"
    # 二进制方式打开图片文件
    for img, file_path in imgs():
        time.sleep(3)
        print(f'开始识别{file_path}')
        params = {"image": img}
        access_token = get_access_token(APIkey='LsXf7qkaFQe5DK12CoWDkbfD',
                                        SecretKey='Tq2Fwtpdr0S6fUa6UouEHElpC9dIWHwW')  # ② access_token
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            for i in response.json()['words_result']:
                print(i['words'])
