# 字符串格式化输出
for i in range(10):
    # 我想打印 :    这是第 i 行
    # 第一种  + 加号拼接字符串
    str1 = '第一种，这是第' + str(i) + '行'
    print(str1)
    # 第二种  f"" {}里面写变量或者语句
    str2 = f"第二种，这是第{i}行"
    print(str2)
    # 第三种
    #  字符串中的%s表示->   %后的变量或表达式
    str3 = "第三种，这是第%s行" % i
    print(str3)
    # 第四种
    # {}大括号表示   .format()  中的变量或表达式
    str4 = "第四种，这是第{}行".format(i)
    print(str4)




