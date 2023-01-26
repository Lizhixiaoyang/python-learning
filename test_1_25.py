# part1—— 查看变量类型
# 1.整数
a = 10
print(type(a))
# python不需要在定义变量的时候显示声明，只是依靠初始化语句根据初始化值的类型来确定
# 在py中，int能够表示的数据范围是无穷的
# 在py中没有long、byte这种类型

# 2.浮点数
b = 2.4
print(type(b))

# C++和java里
# float是四个字节的，也叫做“单精度浮点数”
# double是八个字节的，也叫做“双精度浮点数”
# 但是在python里，float就是双精度浮点数

# 3.字符串
# python中要求使用引号（单双皆可）将一系列字符引起来
c = 'hello'
print(type(c))

# 如果同时有单引号和双引号，就使用三引号

# 求字符串长度——len
length = len(c)
print(length)

# 字符串相加——字符串+字符串，类型不同不能想加
a1='aaa'
a2='bbb'
print(a1+a2)

# 4.bool ——取值为0或1
e = True
print(type(e))



# part2——类型声明(就算标了，后期改了还是会跟着改类型，与C++不同）
a:int = 10
print(type(a))

a:str = 'aaa'
print(type(a))







