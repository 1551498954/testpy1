# a=10
# b=10
#
# print(id(a),id(b))
# a="""
# 111
# 222
#
# 232
#
# 21321
# 412241
# """
# print(a)
import math

c=r"test\nttest"  #转义字符  r:取消转义
print(c)


a=1001
b=456
c=a*b
print(a/b)


#对"789"每一个进行迭代并永和int（）函数转换为int类型
a,b,c=map(int,str(789))
print(a,b,c)




#range()函数 范围函数

range(10)  #默认从0到9 左闭右开

range(10,100) #从10开始
for i in range(3,5):
    print(i)

l=list(range(5))
print(len(l))
print(l.pop())
print(l.pop())
print(l.pop())
print(l.pop())
print(l.pop())

import random
lit=list(range(1,46))
print(lit)

random.shuffle(lit)
print(lit)


# b=random.randint(1,100)
#
# print(b)
#
#
# c=input("请输入c的值：")
#
# print(type(int(c)))

print(math.sin(math.pi))



