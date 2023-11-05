# -*- coding: utf-8 -*-

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
# def function2(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         print(start_time)
#         res = func(*args, **kwargs)
#         time.sleep(0.2)
#         end_time = time.time()
#         print(end_time - start_time)
#         return res
#
#     return wrapper


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
# class A:
#     count = 0
#     def __init__(self, name=20):
#         A.count += 1
#
#     def _hel(self):
#         print('hel')
#
# class B(A):
#     def run(self):
#         self._hel()
#
# a = A()
# b = B()
# b.run()
# print(a._A__hel())
# print(A.__dict__)


# class A:
#     __age = 10
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, new_age):
#         if type(new_age) is not int:
#             print('请输入整数')
#         elif not 0<=new_age<150:
#             print('年龄不对')
#         else:
#             self.__age = new_age
#             print(f'age设置为{new_age}')
#
#     @age.deleter
#     def age(self):
#         del self.__age
#         print('删除age')
#
#
# a = A()
# print(id(a.age))
# print(id(A.age))
# print(a.age)
# a.age = 20
# print(a.age)
# del a.age
# print(a.age)
# print(id(a.age))
# print(id(A.age))

# class P1:
#     def age(self):
#         print('p1')
#
#
# class P2:
#     # def age(self):
#     #     print('p2')
#     def name(self):
#         print('p2')
#         self.age()
# class Kid(P2,P1):
#     ...
#     # def age(self):
#     #     print('kid')
#
# k = Kid()
# k.name()
# print(Kid.mro())


class Fowl:
    def f1(self):
        print('Fowl的F1')


class SwimMixin:
    def swiming(self):
        print('游泳')
    def f1(self):
        print('SwimMixin的F1')
        super().f1()

class Chicken(Fowl):
    def f1(self):
        print('Chicken的F1')


class Duck(SwimMixin, Chicken):
    ...
d = Duck()
d.f1()

class Goose(SwimMixin, Fowl):
    ...
