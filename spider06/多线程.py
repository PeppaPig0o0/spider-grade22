"""
多线程：threading
一个进程中可以同时运行多个线程，这些线程共享资源和空间
（GIL：全局解释器锁。因为GIL存在，所以一个进程中，同一个时刻只有一个线程在执行）
(所以python的多线程是假的)
"""
# import threading
# import time
# def 杨晴():
#     for i in range(1, 51):
#         print(f'杨晴：这是{i}')
#         time.sleep(0.1)
# def 杨亚楠():
#     for i in range(51, 101):
#         print(f'杨亚楠：这是{i}')
#         time.sleep(0.25)
# if __name__ == '__main__':
#     print('这是主线程/函数')
#     # threading.Thread(target=目标函数, name=线程名, args=列表参数, kwargs=字典参数)
#     t1 = threading.Thread(target=杨晴)  # 定义线程1
#     t2 = threading.Thread(target=杨亚楠)  # 定义线程2
#     t1.start()  # 线程1 开始运行
#     t2.start()  # 线程2 开始运行

"""
案例2：赛跑
三位同学赛跑100米，速度不同（10，5，8）
看那位同学先跑到终点
"""
import time
import threading
def run(v):
    for i in range(50):
        # 打印线程名字 threading.current_thread().name
        print(f'{threading.current_thread().name} 跑到第{i}米')
        time.sleep(1/v)
    print(f'{threading.current_thread().name} 跑完啦！')

if __name__ == '__main__':
    # target目标函数 ， name 线程名字，  args参数
    t1 = threading.Thread(target=run, name='杨晴', args=(10, ))
    t2 = threading.Thread(target=run, name='孔灿湘', args=(5,))
    t3 = threading.Thread(target=run, name='李明君', args=(8,))
    t1.start()
    t2.start()
    t3.start()















