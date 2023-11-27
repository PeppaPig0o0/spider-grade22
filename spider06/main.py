# def mmm(a: int, b: int):
#     for i in range(a, 0, -1):
#         if a%i==0 and b%i==0:
#             return f'{a//i}/{b//i}'
#
# N = int(input())
# arr = input().split()
#
# big_fenmu = 1
# big_fenzi = 0
# fenmu = [int(string.split('/')[1]) for string in arr]
# for j in fenmu:
#     big_fenmu = big_fenmu * j
#
# fenzi = [int(string.split('/')[0])*(big_fenmu/int(string.split('/')[1])) for string in arr]
#
# for k in fenzi:
#     big_fenzi = big_fenzi + int(k)
# z = big_fenzi // big_fenmu
# if big_fenzi % big_fenmu == 0:
#     s = f'{z}'
# elif z:
#     s = f'{z} {mmm(big_fenzi % big_fenmu, big_fenmu)}'
# else:
#     s = f'{mmm(big_fenzi % big_fenmu, big_fenmu)}'
# print(s)
#
#

dic = {
    '0': '1',
    '1': '0',
    '2': 'X',
    '3': '9',
    '4': '8',
    '5': '7',
    '6': '6',
    '7': '5',
    '8': '4',
    '9': '3',
    '10': '2',
}
a = (7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)
N = int(input())
ids = [input() for i in range(N)]
wrong = []
for i in ids:
    weight = 0
    for k, v in enumerate(i[:17]):
        if not v.isdigit():
            wrong.append(i)
            break
        weight += a[k] * int(v)

    # print(dic[str(weight % 11)], i[-1])

    if dic[str(weight % 11)] != i[-1]:
        if i not in wrong:
            wrong.append(i)

[print(w) for w in wrong] if wrong else print('All passed')







