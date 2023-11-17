import random
import time
import pymysql


class Mysql:
    def __init__(self,
                 host: str = 'localhost',  # 数据库地址
                 user: str = 'root',  # 链接用户名
                 password: str = '007741ak',  # 链接密码
                 port: int = 3306,  # 端口
                 database: str = 'spider07') -> None:  # 库名字
        self.cursor = None
        self.conn = None
        self.__host = host
        self.__user = user
        self.__password = password
        self.__port = port
        self.__database = database
        self.__run()

    def __run(self) -> None:
        self.conn = pymysql.connect(host=self.__host,
                                    user=self.__user,
                                    password=self.__password,
                                    port=self.__port,
                                    database=self.__database)
        self.cursor = self.conn.cursor()  # 游标对象
        self.conn_id = str(int(time.time())) + ''.join(random.sample(['X', 'Y', 'M', 'R', 'K', 'W', 'G'], 2))
        print('''<- 数据库链接{}开启 ->
用户名:{} 端口:{} 接入数据库:{}'''.format(
            self.conn_id,
            self.__user,
            self.__port,
            self.__database))

    def __del__(self) -> None:
        self.cursor.close()
        self.conn.close()
        print(f'<- 数据库链接{self.conn_id}关闭 ->')


cnki = Mysql()
sql = 'select * from zhiwang'
cnki.cursor.execute(sql)
cnki.conn.commit()
res = cnki.cursor.fetchall()
print(res)
