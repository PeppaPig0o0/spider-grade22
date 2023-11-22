# def mmm(a: int, b: int):
#     for i in range(a, 0, -1):
#         if a%i==0 and b%i==0:
#             return f'{a//i}/{b//i}'
#
# N = int(input())
# arr = input().split()
#
#
# big_fenmu = 1
# big_fenzi = 0
# # fenmu = [int(string.split('/')[1]) for string in arr]
# fenmu = list(map(lambda string: int(string.split('/')[1]), arr))
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



# students = [
#             {"name": "John Doe",
#              "father name": "Robert Doe",
#              "Address": "123 Hall street"
#              },
#             {
#               "name": "Rahul Garg",
#               "father name": "Kamal Garg",
#               "Address": "3-Upper-Street corner"
#             },
#             {
#               "name": "Angela Steven",
#              "father name": "Jabob steven",
#              "Address": "Unknown"
#             }
# ]
#
# print(list(map(lambda student: student['name'], students)))
# # print(list(map(lambda st)))

# fruits = [30, 20, 10, 17, 15]
# print(list(filter(lambda fruit: fruit%5==0, fruits)))