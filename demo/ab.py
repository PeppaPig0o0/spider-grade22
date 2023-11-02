# def func1():
#     def outer():
#         def warper():
#             # 代码1
#             res = func():
#
#
#
# def go():
#     print('go')
import time


# 无参装饰器
def function2(func):
    def warpper(*args, **kwargs):
        start_time = time.time()
        print(start_time)
        res = func(*args, **kwargs)
        time.sleep(0.2)
        end_time = time.time()
        print(end_time - start_time)
        return res

    return warpper


# @func1
# def go():
#     print('go')
#
# @func1
# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
#
# print(add(1, 3, 5))


# 有参数装饰器
# def function1(user, pwd):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             print(user, pwd)
#             if user == 'a' and pwd == 'a':
#                 print(2, user, pwd)
#                 res = func(*args, **kwargs)
#                 print(3, user, pwd)
#                 return res
#             else:
#                 print('错误')
#
#         return wrapper
#
#     return outer
#
#
# @function2
# @function1(user=input('用户名:'), pwd=input('密码:'))  # a a    b b
# @function1(user=input('用户名:'), pwd=input('密码:'))  # b b    a a
# def home(user):
#     print(f'欢迎{user}')
#
#
# home('b')

# dic = {
#     'a': 12,
#     'b': 17,
#     'ab': 14,
#     'bb': 15,
# }
#
#
# def f(k):
#     return dic[k]
#
#
# res = max(dic, key=lambda k: dic[k])
# print(res)
# l = [(1, 3), (2, 5), (1, 6), (1, 4)]
# # l.sort(key=lambda item: item[1])
#
# print(sorted(l, key=lambda item: item[1]))
# print(l)


l = ['哈哈', '哈哈1', '哈哈2', '哈哈3']
a = map(lambda i: i+'123', l)
print(a)

