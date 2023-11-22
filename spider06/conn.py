import pymysql
class Conn:
    def __init__(self, **kwargs):
        self.host = kwargs.get('host', 'localhost')
        self.user = kwargs.get('user', 'root')
        self.password = kwargs.get('password', '007741ak')
        self.port = kwargs.get('port', 3306)
        self.database = kwargs.get('database', 'spider06')
        self.conn = None
        self.cursor = None
        self.__run()

    def __run(self):
        try:
            self.conn = pymysql.connect(host=self.host,  # 数据库地址
                                        user=self.user,  # 用户名
                                        password=self.password,  # 密码
                                        port=self.port,  # 端口号
                                        database=self.database)  # 数据库名
            self.cursor = self.conn.cursor()
            print(f'数据库{self.database}->用户名{self.user}链接成功')
        except:
            print('链接失败，请检查链接信息')

    def __del__(self):
        if self.cursor and self.conn:
            self.cursor.close()
            self.conn.close()
            print('数据库链接关闭')
        else:
            print('数据库链接异常，已关闭')


from pymongo import MongoClient

class MongoDB:
    def __init__(self, database, host="localhost", port=27017):
        self.client = MongoClient(host, port)
        self.db = self.client[database]

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def close(self):
        self.client.close()


if __name__ == '__main__':
    c = Conn()
    sql = 'SELECT * FROM zhiwang'
    c.cursor.execute(sql)
    res = c.cursor.fetchall()
    print(res)

