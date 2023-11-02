def func1():
    print(a+b)

def func2():
    print('这是func2 函数')

# py文件运行时,会先运行主函数
# 主函数内定义的变量是全局变量
# 其他文件引入该文件时，主函数内容不执行
if __name__ == '__main__':
    print('这是主函数')
    a, b = 10, 20
    func1()
    func2()














