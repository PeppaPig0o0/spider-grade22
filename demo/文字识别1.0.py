import random
import time

import pymysql.err
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
        self.db = Conn()

    def get_key(self):
        sql = 'SELECT apikey,secretkey FROM ocr_keys where vaild=1'
        self.db.cursor.execute(sql)
        res = self.db.cursor.fetchall()
        return random.choice(res)

    def set_key(self):
        print('请输入你的百度图片识别应用的APIKey和SecretKey')
        while True:
            apikey = input('APIKey:')
            secretkey = input('SecretKey:')

            access_token = Authenticate().get_access_token(apikey, secretkey)
            if access_token:
                break
            print('你输入的信息有误，请查证后再输入')

        try:
            sql = f"INSERT INTO ocr_keys(apikey, secretkey, vaild) VALUE('{apikey}', '{secretkey}', 1)"
            self.db.cursor.execute(sql)
            self.db.conn.commit()
            print('校验成功，已收录')
        except pymysql.err.IntegrityError:
            print('该APIKey已存在。')

class Authenticate:
    access_token_url = "https://aip.baidubce.com/oauth/2.0/token"

    def __init__(self):
        # self.access_token = self.get_access_token(*Keys().get_key())
        self.access_token = None

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
        # print(response.json())
        if response.json().get('error') == 'invalid_client':
            return None
        self.access_token = response.json()['access_token']
        return self.access_token

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
    print('程序启动中，请稍后.....')
    c = Ocr()
    c.run()



