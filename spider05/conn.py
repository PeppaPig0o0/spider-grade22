import pymysql


class Conn:
    """
    mysql数据库链接
    参数: host 默认值localhost
    参数: user 默认值 root
    参数: password 默认值 007741ak
    参数: port 默认值 3306
    参数: database 默认值 spider05
    """
    def __init__(self, **kwargs):
        """
        构造函数：实例化对象时，自动调用
        """
        self.__host = kwargs.get('host', 'localhost')
        self.__user = kwargs.get('user', 'root')
        self.__password = kwargs.get('password', '007741ak')
        self.__port = kwargs.get('port', 3306)
        self.__database = kwargs.get('database', 'spider05')
        self.conn, self.cursor = None, None
        self.__run()

    def __run(self):
        self.conn = pymysql.connect(host=self.__host,
                                    user=self.__user,
                                    password=self.__password,
                                    port=self.__port,
                                    database=self.__database)
        self.cursor = self.conn.cursor()
        print(f'数据库{self.__database}链接成功,用户{self.__user}')

    def __del__(self):
        """
        析构函数：结束对象引用时/销毁对象时，自动调用
        """
        if self.conn and self.cursor:
            self.cursor.close()
            self.conn.close()
            print('数据库链接关闭')
        else:
            print('数据库链接异常，已关闭')


if __name__ == '__main__':
    db = Conn()
    sql = 'SELECT * FROM zhiwang'
    db.cursor.execute(sql)
    res = db.cursor.fetchall()
    print(res)



