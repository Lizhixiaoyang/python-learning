# part1 算术运算符
# 先乘方再乘除后加减
# 在python中，不允许0作为除数，会抛出异常
  ## print(10/0)
# 在python中，整数除整数，结果可能是小数
  ## print(10/3)  #3.3333333333333335
# 求余数——%
  ## print(10 % 3)
# 乘方——**
  ## print(2**3)
  ## print(2**0.5)
# 地板除法（取整除法）——//，对计算结果向下取整
  ## print(7//2)  # 3
  ## print(-7//2) # -4


# part2——关系运算符（比较两个操作符之间的关系，如大小、相等）
# 不光可以针对数字进行 比较，字符串也可以比
#  大于 >      小于 <
#  大于等于>=   小于等于<=
#  相等 ==     不相等 !=

# a='abandon'
# b='apple'
# print(a > b) # 返回True、False
# print(a!=b)

# 针对浮点数，使用==比较有风险
## print(0.1+0.2 == 0.3)  #false


# part3——逻辑运算符
# 并且 and    有车且有房，缺一不可
# 或者 or     有车或有房，一样即可
# 逻辑取反 not

# a = 10
# b = 20
# c = 30
# print(a < b and b < c)
# print(a > b or b < c)
# print(not a > b)


# part4 —— 赋值操作符
# 赋值 =

#多元赋值
# a = 10
# b = 20
# a, b = b, a  # 进行交换
# print(a, b)


# python不支持++ --
# 它只会当成正号负号




