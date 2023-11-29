import random
import time

# encoding:utf-8

import requests
import base64
import requests
import json
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image
from conn import Conn

class Keys:
    def __init__(self):


    @classmethod
    def get_key(cls):
        db = Conn()
        sql = 'SELECT apikey,secretkey FROM ocr_keys where vaild=1'
        db.cursor.execute(sql)
        res = self.cursor.fetchall()
        return random.choice(res)


    def set_key(self):
        db = Conn()
        apikey = input('输入apikey:')
        secretkey = input('输入secretkey:')
        sql = 'SELECT apikey,secretkey FROM ocr_keys where vaild=1'
        sql = 'INSERT INTO ocr_keys(apikey,secretkey,vaild) VALUE ()'
        db.cursor.execute(sql)
        res = self.cursor.fetchall()
        return random.choice(res)


class Authenticate:
    access_token_url = "https://aip.baidubce.com/oauth/2.0/token"

    def __init__(self):
        self.access_token = self.get_access_token(*Keys.get_key())

    def get_access_token(self, apikey, secretkey):
        params = {
            'client_id': apikey,  # API Key
            'grant_type': 'client_credentials',
            'client_secret': secretkey  # Secret Key
        }
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        # 这里需要再判断access_token是否能用
        response = requests.post(Authenticate.access_token_url, params=params, headers=headers)
        access_token = response.json()['access_token']
        return access_token

    def __str__(self):
        return self.access_token


class Ocr:
    ALLOW_IMG_FORMAT = ['jpg', 'jpeg', 'png', 'bmp']
    MAX_SIZE = 111111
    MAX_PIX = 8192
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate"

    def __init__(self):
        self.files_path = []
        self.select_images()
        self.run()

    def run(self):
        access_token = Authenticate().access_token
        request_url = Ocr.request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}

        for img in self.get_img():
            params = {"image": img}
            response = requests.post(request_url, data=params, headers=headers)
            if response:
                print(response.json())
                for i in response.json()['words_result']:
                    print(i['words'])

    def select_images(self):
        while True:
            path = filedialog.askopenfilename()
            if path == '':
                break
            if path.rsplit('.')[-1] not in Ocr.ALLOW_IMG_FORMAT:
                messagebox.showerror(title='错误', message=f'图片必须是{"/".join(Ocr.ALLOW_IMG_FORMAT)}格式,请重新选择')
                continue
            self.files_path.append(path)


    def get_img(self):
        for file_path in self.files_path:
            # 打开图片
            image = Image.open(file_path)

            width, height = image.size
            if max(width, height) > Ocr.MAX_PIX:
                per = Ocr.MAX_PIX / max(width, height)
                image = image.resize((int(width * per - 1), int(height * per - 1)), Image.LANCZOS)
                image.save(file_path)

            with open(file_path, 'rb') as f:
                yield base64.b64encode(f.read())


if __name__ == '__main__':
    c = Ocr()
    c.run()



