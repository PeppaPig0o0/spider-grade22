"""
多线程：threading
一个进程中可以同时运行多个线程，这些线程共享资源和空间
（GIL：全局解释器锁。因为GIL存在，
所以一个进程中，同一个时刻只有一个线程在执行）
(所以python的多线程是假的)
"""
# # threading 是标准库
# import threading
# # 语法
# threading.Thread(target=目标函数, name='线程名', args=(参数,), kwargs=字典参数)

# 案例1
# import threading
# import time
# def 杨洋():
#     for i in range(1, 51):
#         print(f'杨洋数{i}')
#         time.sleep(0.1)
# def 李婉君():
#     for i in range(51, 101):
#         print(f'李婉君数{i}')
#         time.sleep(0.15)
# if __name__ == '__main__':
#     print('开始')
#     t1 = threading.Thread(target=杨洋)
#     t2 = threading.Thread(target=李婉君)
#     t1.start()
#     t2.start()

# 案例2
# import threading
# import time

# def run(v):
#     for i in range(20):
#         # threading.current_thread().name 当前线程的名字
#         print(f'{threading.current_thread().name}跑了{i}米')
#         time.sleep(1/v)
#     print(f'{threading.current_thread().name}跑完了！')
#
# if __name__ == '__main__':
#     print('开始')
#     member = {'杨洋': 5, '李婉君': 8, '丁旭': 10, '王嘉庚': 15}
#     a = {}
#     for key, value in member.items():
#         a[key] = threading.Thread(target=run, name=key, args=(value, ))
#         a[key].start()
#     print(a)
#     for i in a.values():
#         i.join()
#     print('结束')














# import time
# import threading
# from tqdm import tqdm
#
# def task_A():
#     for _ in tqdm(range(100), desc="ad"):
#         time.sleep(0.1)
#
# def task_B():
#     for _ in tqdm(range(100), desc="da"):
#         time.sleep(0.1)
#
# if __name__ == '__main__':
#     thread_A = threading.Thread(target=task_A)
#     thread_B = threading.Thread(target=task_B)
#
#     thread_A.start()
#     thread_B.start()
#
#     thread_A.join()
#     thread_B.join()

import threading,time

class Demo(threading.Thread):

    def run(self):
        print(f'子线程{self.name}开始...')  # 继承Thread后， 可以调Thread的方法name来获取当前线程名字
        time.sleep(2)
        print(f'{self.is_alive()}')
        print(f'子线程{self.name}结束...')


if __name__ == '__main__':
    print('主线程开始...')
    threads = [Demo(name=f'{i}哈哈', daemon=True) for i in range(3)]  # 创建3个线程对象
    for t in threads:
        t.start()

    print('123')
    # for t in threads:
    #     t.join()


