# -*- coding: utf-8 -*-

import pymysql


class Conn:
    def __init__(self, **kwargs) -> None:
        self.__host = kwargs.get('host', 'localhost')  # 数据库地址
        self.__user = kwargs.get('user', 'root')  # 链接用户名
        self.__password = kwargs.get('password', '007741ak')  # 链接密码
        self.__port = kwargs.get('port', 3306)  # 链接端口
        self.__database = kwargs.get('database', 'spider08')  # 接入数据库名字
        self.conn = None
        self.cursor = None
        self.__run()

    def __run(self) -> None:
        """
        开启数据库链接
        """
        try:
            self.conn = pymysql.connect(host=self.__host,
                                        user=self.__user,
                                        password=self.__password,
                                        port=self.__port,
                                        database=self.__database)
            self.cursor = self.conn.cursor()
            print(f'数据库链接开启->用户名{self.__user}->数据库{self.__database}')
        except:
            print('链接失败，请检查链接信息')

    def __del__(self) -> None:
        if self.conn and self.conn:
            self.cursor.close()
            self.conn.close()
            print('关闭数据库链接')
        else:
            print('数据库链接异常，已关闭')


if __name__ == '__main__':
    c = Conn()
    sql = 'select * from zhiwang'
    c.cursor.execute(sql)
    res = c.cursor.fetchone()
    print(res)
