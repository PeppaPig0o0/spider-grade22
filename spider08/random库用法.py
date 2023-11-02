# """
# random库的学习和使用
# random是python标准库用于生成随机数、随机整数、还有随机从数据集取数据
# """
import random

# ① random.random() 生成0-1之间随机浮点数
a = random.random()
print(f'a是{a}')

# ② random.randint(小整数, 大整数)
# 从两个整数之间生成一个随机整数。可以取到最小值和最大值
b = random.randint(51, 187)
print(f'b是{b}')

# ③ random.uniform(整数\浮点数, 整数\浮点数)
# 从两个数字之间生成一个随机浮点数。
c = random.uniform(0.5, 2)
print(f'c是{c}')

# ④ random.randrange(0, 100, 10)
# 从指定最大最小值之间，根据步长进行随机。最大值取不到
d = random.randrange(0, 100, 10)
print(f'd是{d}')

# ⑤ random.choice() 从字符串或列表中随机选一个字符
# random.choices() 从字符串或列表中随机选k个字符
e = random.choice('22高职计算机8班')
print(f'e是{e}')
f = random.choice(['任移旺', '郑大川', '孙玉松', '丁旭'])
print(f'f是{f}')
g = random.choices(['任移旺', '郑大川', '孙玉松', '丁旭'], k=2)
print(f'g是{g}')

# ⑥ random.shuffle() 打乱列表或字符串，修改原对象，返回
h = ['hehe', 'xixi', 'heihei', 'haha', 'zhizhi']
random.shuffle(h)
print(h)
m = [1, 2, 3, 4, 5]
random.shuffle(m)
print(m)

# ⑦ random.sample(列表, 长度)  根据长度从列表、字符串中随机切片
list1=[1,2,3,4,5,6,7,8,9,10]
slice=random.sample(list1,5)
print(slice)
x = random.sample(range(0, 10), 5)
print(x)
Words = "AppleKMedoide"
print(random.sample(Words, 3))
print(random.sample(Words, 3))


