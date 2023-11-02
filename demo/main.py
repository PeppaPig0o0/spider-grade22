# import requests
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
#     'Referer': 'http://www.htqyy.com/top/hot',
#     'Cookie': 'Hm_lvt_74e11efe27096f6ef1745cd53f168168=1697003520; blk=0; isPlay=0; jploop=false; Hm_lpvt_74e11efe27096f6ef1745cd53f168168=1697011830',
# }
# ranks = ['http://www.htqyy.com/top/musicList/hot',
#          'http://www.htqyy.com/top/musicList/new',
#          'http://www.htqyy.com/top/musicList/recommend',
#          'http://www.htqyy.com/genre/musicList/1',
#          'http://www.htqyy.com/genre/musicList/3',
#          'http://www.htqyy.com/genre/musicList/5']
# for rank in ranks:
#     for i in range(0, 25):
#         url = f'{rank}?pageIndex={i}&pageSize=20'
#         with requests.get(url=url, headers=headers) as response:
#             print(response.text)


import asyncio
import random
import time


#
# # 去生成或获取一个事件循环
# loop = asyncio.get_event_loop()
#
# # 将任务放到“任务列表”中
# loop.run_until_complete(任务)


# async def rand_int():
#     print(1)
#     await asyncio.sleep(2)
#     print(2)
#
#
#
#
# tasks = [rand_int() for i in range(2)]
# asyncio.run(asyncio.wait(tasks))
#
# async def rand_int():
#     print(1)
#     await asyncio.sleep(2)
#     print(2)
#     return '返回'
#
#
# async def func():
#     print('开始')
#     task1 = asyncio.create_task(rand_int())
#     task2 = asyncio.create_task(rand_int())
#     print('结束')
#     r1 = await task1
#     r2 = await task2
#     print(r1, r2)
#
# asyncio.run(func())


# def func():
#     print('生成器函数')
#     a = 1
#     while True:
#         yield a
#         a += 1
#
# obj = func()
# for i in range(5):
#     print(next(obj))

# import time
#
# def func_a():
#     while True:
#         print(f'生成器函数{func_a.__name__}')
#         yield
#         time.sleep(2)
#
#
# def func_b(obj):
#     while True:
#         print(f'生成器函数{func_b.__name__}')
#         obj.__next__()
#
#
# a = func_a()
# func_b(a)

import time
# def func(i):
#     time.sleep(1)
#     print(i)
# now = lambda: time.time()
# start = now()
# for i in range(5):
#     func(i)
# print(f'花费时间为{now()- start}')

# import time
# import asyncio
#
# now = lambda : time.time()
# start = now()
#
# async def func(i):
#     asyncio.sleep(1)
#     print(i)
#
# for i in range(5):
#     asyncio.run(func(i))
#
# print(f'花费时间为{now()- start}')

# import asyncio
#
# async def work1():
#     for _ in range(5):
#         print('协程1')
#         time.sleep(1)
#         await asyncio.sleep(1)
#
# async def work2():
#     for _ in range(5):
#         print('协程2')
#         await asyncio.sleep(1)

# async def main():
#     # await asyncio.gather(work1(), work2())
#     # tasks = [work1(),work2()]
#     tasks = [asyncio.create_task(work1()), asyncio.create_task(work2())]
#     await asyncio.wait(tasks)
# asyncio.run(main())

#
# import asyncio
# async def work(n):
#     print('work启动')
#     await asyncio.sleep(3)
#     print('work完成')
#     return f'协程任务{n}'
#
# tasks = [work(1), work(2)]
# asyncio.run(asyncio.wait(tasks))
# async def main():
#     # tasks = [asyncio.create_task(main()), asyncio.create_task(main())]
#     # task1 = asyncio.create_task(work())
#     # task2 = asyncio.create_task(work())
#     tasks = [asyncio.create_task(work(i)) for i in range(5)]
#     res = await asyncio.gather(*tasks)
#
#     # done, pending = await asyncio.wait(tasks)
#     # print(pending)
#     for i in res:
#         print(i)
#     # print(456)
#     # r1 = await task1
#     # r2 = await task2
#     # print(r1)
#     # print(r2)
#
# asyncio.run(main())

import asyncio
asyncio.set_event_loop()


