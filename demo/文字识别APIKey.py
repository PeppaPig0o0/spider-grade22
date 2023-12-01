import random
import time

import pymysql.err
import requests
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

    def password(self):




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

        if response.json().get('error') == 'invalid_client':
            return None
        self.access_token = response.json()['access_token']
        return self.access_token

    def __str__(self):
        return self.access_token


if __name__ == '__main__':
    Keys().set_key()
    print('三秒钟后程序结束....')
    time.sleep(3)


