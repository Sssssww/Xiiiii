import math
import random

#input()输入函数
num = input("输入一个数：")
if num.isdigit():
    num = int(num)
    if 100 < num < 999:
        print('这是三位数')
        pass
    else:
        print("请输入一个三位数")