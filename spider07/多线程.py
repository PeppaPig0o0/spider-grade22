"""
多线程：threading
一个进程中可以同时运行多个线程，这些线程共享空间和资源
GIL：全局解释器锁。因为GIL存在，所以一个进程中，
同一个时刻只有一个线程在执行
(所以python的多线程是假的)
"""
# import threading
# import time
# def 徐勇梅():
#     for i in range(1, 51):
#         print(f'徐勇梅数{i}')
#         time.sleep(0.1)
# def 李永娜():
#     for i in range(51, 101):
#         print(f'李永娜数{i}')
#         time.sleep(0.1)
# if __name__ == '__main__':
#     print('开始')
#     t1 = threading.Thread(target=徐勇梅, name='徐勇梅')
#     t2 = threading.Thread(target=李永娜, name='李永娜')
#     t1.start()
#     t2.start()

import threading
import time
def run(v):
    for i in range(50):
        # threading.current_thread().name  当前线程的名字
        print(f'{threading.current_thread().name}跑到第{i}米')
        time.sleep(1/v)
    print(f'{threading.current_thread().name}跑完了')
if __name__ == '__main__':
    print('开始！')
    t1 = threading.Thread(target=run, name='徐勇梅', args=(5,))
    t2 = threading.Thread(target=run, name='李永娜', args=(8,))
    t3 = threading.Thread(target=run, name='叶红', args=(10,))
    t4 = threading.Thread(target=run, name='胡省慧', args=(12,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()

# def run():
#     while arr:
#         print(f'{threading.current_thread().name}-{arr.pop()}')
#
# if __name__ == '__main__':
#     print('开始！')
#     arr = [i for i in range(2000)]
#     for i in range(10):
#         threading.Thread(target=run, name=f'{i}').start()
#     t1 = threading.Thread(target=run, name='徐勇梅', args=(5,))
#     t2 = threading.Thread(target=run, name='李永娜', args=(8,))
#     t3 = threading.Thread(target=run, name='叶红', args=(10,))
#     t4 = threading.Thread(target=run, name='胡省慧', args=(12,))
#     t1.start()
#     t2.start()
#     t3.start()
#     t4.start()

