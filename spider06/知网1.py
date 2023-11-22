"""
案例:知网
使用selenium驱动浏览器窗口，搜索关键词。
获取论文的标题、作者和简介。
"""
# ① 引入库(selenium库)
import time
import random
import asyncio
from selenium.common import exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By

from conn import Conn, MongoDB
#
# class C:
#     async def __new__(cls, *args, **kwargs):
#         instance = super().__new__(cls)
#         await instance.__init__(*args, **kwargs)
#         return instance
#
#     async def __init__(self):
#         for i in range(5):
#             await asyncio.sleep(1)
#             print('c')
#
# class Z:
#     def __init__(self, n):
#         pass
#
#     @classmethod
#     async def init_run(cls, number):
#         self = cls(number)
#         await self.__run()
#         return self
#
#     async def __run(self):
#         await C()
#
#
# async def main():
#     tasks = [asyncio.create_task(Z.init_run(i)) for i in [1, 2, 3, 4]]
#     res = await asyncio.gather(*tasks)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())
#




class Zi:
    service = webdriver.ChromeService(executable_path='chromedriver.exe')

    async def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        await instance.__init__(*args, **kwargs)
        return instance

    async def __init__(self, n):
        self.n = n
        self.browser = webdriver.Chrome(service=Z.service)
        self.db = Conn()
        await self.__run()

    async def __run(self):
        await asyncio.sleep(2)
        # self.browser.get
        self.browser.get('https://www.cnki.net')
        await asyncio.sleep(5)
        self.browser.find_element(By.ID, 'txt_SearchText').send_keys('英雄联盟')
        await asyncio.sleep(0.5)
        self.browser.find_element(By.CLASS_NAME, 'search-btn').click()
        await asyncio.sleep(5)
        # ⑤ 提取网页信息
        for i in range(self.n, 30, 4):
            try:
                self.browser.find_element(By.XPATH, f'//a[@data-curpage="{i}"]').click()
            except exceptions.NoSuchElementException:
                print('采集完成')
                break
            await asyncio.sleep(5)
            tr_list = self.browser.find_elements(By.XPATH, '//*[@id="gridTable"]/div/div/table/tbody/tr')
            for tr in tr_list[-1:]:
                # self.parse_one(tr)  # 提取一条论文数据
                await self.parse_one(tr)

    async def parse_one(self, element):
        a_title = element.find_element(By.CLASS_NAME, 'fz14')  # 论文标题
        title = a_title.text
        a_list = element.find_elements(By.CLASS_NAME, 'KnowledgeNetLink')
        authors = ','.join([a.text for a in a_list])  # 论文作者
        source = element.find_element(By.XPATH, '//td[@class="source"]/p/a').text  # 论文来源
        public_date = element.find_element(By.CLASS_NAME, 'date').text  # 论文发表时间
        # ⑥ 点击并切换到新标签页
        a_title.click()
        await asyncio.sleep(0.5)
        self.browser.switch_to.window(self.browser.window_handles[1])
        # ⑦ 提取内容页的信息
        await asyncio.sleep(5)
        abstract = self.browser.find_element(By.CLASS_NAME, 'abstract-text').text  # 摘要/正文快照
        keywords = self.browser.find_elements(By.NAME, 'keyword')
        keywords = ','.join([k.text for k in keywords])  # 关键词
        #  ⑧ 打印结果，并存储到mysql数据库
        print(title, authors, source, public_date)
        print(abstract, keywords)
        # sql语句
        sql = f'''
                INSERT INTO zhiwang(title, authors, source, public_date, abstract, keywords)
                VALUES('{title}', '{authors}', '{source}', '{public_date}', '{abstract}', '{keywords}')
                '''
        self.db.cursor.execute(sql)  # 提交到数据库
        self.db.conn.commit()
        self.browser.close()  # 关闭标签页
        # ⑨ 切换回原标签页
        self.browser.switch_to.window(self.browser.window_handles[0])
        await asyncio.sleep(1)

    def __del__(self):
        self.browser.quit()
        del self.db



class Z:
    service = webdriver.ChromeService(executable_path='chromedriver.exe')

    async def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        await instance.__init__(*args, **kwargs)
        return instance

    async def __init__(self, n):
        self.n = n
        self.browser = webdriver.Chrome(service=Z.service)
        # self.db = MongoClient('mongodb://localhost:27017/')
        self.db = MongoDB('spider06')
        self.db.get_collection('zhiwang')
        await self.__run()

    async def __run(self):
        await asyncio.sleep(2)
        # self.browser.get
        self.browser.get('https://www.cnki.net')
        await asyncio.sleep(5)
        self.browser.find_element(By.ID, 'txt_SearchText').send_keys('英雄联盟')
        await asyncio.sleep(0.5)
        self.browser.find_element(By.CLASS_NAME, 'search-btn').click()
        await asyncio.sleep(5)
        # ⑤ 提取网页信息
        for i in range(self.n, 30, 4):
            try:
                self.browser.find_element(By.XPATH, f'//a[@data-curpage="{i}"]').click()
            except exceptions.NoSuchElementException:
                print('采集完成')
                break
            await asyncio.sleep(5)
            tr_list = self.browser.find_elements(By.XPATH, '//*[@id="gridTable"]/div/div/table/tbody/tr')
            for tr in tr_list[-1:]:
                # self.parse_one(tr)  # 提取一条论文数据
                await self.parse_one(tr)

    async def parse_one(self, element):
        a_title = element.find_element(By.CLASS_NAME, 'fz14')  # 论文标题
        title = a_title.text
        a_list = element.find_elements(By.CLASS_NAME, 'KnowledgeNetLink')
        authors = ','.join([a.text for a in a_list])  # 论文作者
        source = element.find_element(By.XPATH, '//td[@class="source"]/p/a').text  # 论文来源
        public_date = element.find_element(By.CLASS_NAME, 'date').text  # 论文发表时间
        # ⑥ 点击并切换到新标签页
        a_title.click()
        await asyncio.sleep(0.5)
        self.browser.switch_to.window(self.browser.window_handles[1])
        # ⑦ 提取内容页的信息
        await asyncio.sleep(5)
        abstract = self.browser.find_element(By.CLASS_NAME, 'abstract-text').text  # 摘要/正文快照
        keywords = self.browser.find_elements(By.NAME, 'keyword')
        keywords = ','.join([k.text for k in keywords])  # 关键词
        #  ⑧ 打印结果，并存储到mongodb数据库
        self.db.get_collection('zhiwang').insert_one(dict(title=title, authors=authors, source=source, public_date=public_date, abstract=abstract, keywords=keywords))
        self.browser.close()  # 关闭标签页
        # ⑨ 切换回原标签页
        self.browser.switch_to.window(self.browser.window_handles[0])
        await asyncio.sleep(1)

    def __del__(self):
        ...
        # self.browser.quit()
        # self.db.close()


async def main():
    start_time = time.time()
    tasks = [asyncio.create_task(Z(i)) for i in range(1, 5)]
    # print(tasks)
    res = await asyncio.gather(*tasks)
    end_time = time.time()
    print(end_time-start_time)




if __name__ == '__main__':
    """
    设置uvloop
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    """
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(main())
    # asyncio.run(main())


