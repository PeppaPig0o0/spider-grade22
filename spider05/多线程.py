"""
多线程：threading
一个进程中可以同时运行多个线程，这些线程共享资源和空间
（GIL：全局解释器锁。因为GIL存在，所以一个进程中，同一个时刻只有一个线程在执行）
(所以python的多线程并不能提高计算效率)
"""
# import threading
# import time
#
# # 案例1——>苗瑞和崔乐乐一起数1-100
# def 苗瑞():
#     for i in range(1, 51):
#         print(f'苗瑞数{i}')
#         time.sleep(0.15)
# def 崔乐乐():
#     for i in range(51, 101):
#         print(f'崔乐乐数{i}')
#         time.sleep(0.1)
# # 语法
# # threading.Thread(target=目标函数, name=线程名, args=(参数1, ), kwargs=字典参数)
# if __name__ == '__main__':
#     print('这是主函数')
#     t1 = threading.Thread(target=苗瑞)  # 新建线程1
#     t2 = threading.Thread(target=崔乐乐)  # 新建线程2
#     t1.start()  # 线程1启动
#     t2.start()  # 线程2启动

# 案例2——> 多人跑50米
import time
import threading
def run(v):
    for i in range(50):
        # threading.current_thread().name  当前线程名字
        print(f'{threading.current_thread().name}跑了{i}米')
        time.sleep(1/v)
    print(f'{threading.current_thread().name}跑完啦！')

if __name__ == '__main__':
    runners = {'马堂景': 10, '刘仁杰': 8, '轩丽娜': 8, '郑梦婷': 6, '程文雅': 6}
    for k, val in runners.items():
        threading.Thread(target=run, name=k, args=(val, )).start()

