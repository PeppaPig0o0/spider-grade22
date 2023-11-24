"""
案例:知网
使用selenium驱动浏览器窗口，搜索关键词。
获取论文的标题、作者和简介。
"""
# ① 引入库(selenium库)
import time
import random
import asyncio
import aiofiles
import aiohttp
from selenium import webdriver



class Z:
    service = webdriver.ChromeService(executable_path='chromedriver.exe')

    async def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        await instance.__init__(*args, **kwargs)
        return instance

    async def __init__(self, n):
        self.n = n
        for i in range(100):
            async with aiohttp.ClientSession() as session:
                async with aiofiles.open(f'./tt/m{self.n}.txt', 'a+', encoding='utf-8') as f:
                    await f.write(''.join(random.choices(str, k=10)))
                    # print(f'{n}-{i}')
                # try:
                #     async with  session.get('https://www.baidu.com', timeout=2) as res:
                #         print(f'Z-{self.n}-{i}')
                # except asyncio.exceptions.TimeoutError:
                #     pass


    def __del__(self):
        ...
        # self.browser.quit()
        # self.db.close()


class X:
    service = webdriver.ChromeService(executable_path='chromedriver.exe')

    async def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        await instance.__init__(*args, **kwargs)
        return instance

    async def __init__(self, n):
        self.n = n
        for i in range(20):
            async with aiohttp.ClientSession() as session:
                try:
                    async with  session.get('https://www.baidu.com', timeout=2) as res:
                        print(f'X-{self.n}-{i}')
                except asyncio.exceptions.TimeoutError:
                    pass

async def main():
    start_time = time.time()
    tasks = [asyncio.create_task(Z(i)) for i in range(1, 50)]
    # tasks += [asyncio.create_task(X(i)) for i in range(1, 10)]
    res = await asyncio.gather(*tasks)
    end_time = time.time()
    print(end_time-start_time)




if __name__ == '__main__':
    str = 'ABCDEDFGHIJKL'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    """
    设置uvloop
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    """
    import uvloop

    # asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(main())
    # asyncio.run(main())

    #10.049206018447876



