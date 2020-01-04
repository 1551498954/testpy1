
#python的空格有作用
import math

while True:
    a=int(input())
    if a<18:
        print('未成年人')
    elif a>=18 and a<35:
        print('年轻人')
    elif a>=35 and a<65:
        print('中年人')
    elif a>=65 and a<200:
        print('老年人')
    else:
        print('真人')