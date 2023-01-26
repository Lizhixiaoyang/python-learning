# # part1——将数字和字符串混合打印
# a = 10
# print(f"a = {a}")  # 格式化字符串
# # 此语法叫格式化字符串 fstring
# # 利用{}这种语法，往字符串里嵌入变量或表达式



# # part2——通过控制台输入数据
# num = input('请输入一个数据')
# print(f'您输入的数字是{num}')

# input的返回值是一个字符串
# 如果只是单纯的拿到用户的输入并打印，按照str打印即可
# 如果想进行算数计算，需要进行类型转换

# # 示例
# a = input('请输入第一个数据：')
# b = input('请输入第二个数据：')
# # 进行算数转换
# a = int(a)
# b = int(b)
# print(f"a+b={a+b}")



#输入四个小数，求四个小数的平均值
a = input('请输入第一个数据：')
b = input('请输入第二个数据：')
c = input('请输入第三个数据：')
d = input('请输入第四个数据：')

a=float(a)
b=float(b)
c=float(c)
d=float(d)

avg=(a+b+c+d)/4
print(f"avg={avg}")




