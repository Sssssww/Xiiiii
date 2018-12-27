
#查看系统保留的关键字，不可被当做变量来命名
import  keyword
print(keyword.kwlist)

import  math
#print(math)
#ceil()向上取整操作
print(math.ceil(5.6668))
print(math.ceil(5.1))

#floor ()向下取整
print(math.floor(5.6668))
print(math.floor(5.1))

#round()四舍五入
print(round(5.001))
print(round(5.125))
print(round(5.524))

# sqrt()开平方 退回浮点数
print(math.sqrt(2))

#pow() 与幂运算差不多，计算一个数的几次方， 有两个参数，第一个为 底数 第二个为 指数
print(math.pow(4,3))#返回浮点数
print(4**3)         #返回整数

# fabs()对一个数取绝对值
print(math.fabs(-87))

#abs()python内置函数 返回值由本身决定
print(abs(-1))

#fsum()对整个序列求和 返回浮点数
print(math.fsum([1,2,3,5,]))
#sum()Python内置函数 返回值有本身决定
print(sum([4,6,3,5]))

#math.modf()将一个浮点数拆分为整数和小数部分   （小数在钱，整数在后）
print(math.modf(4.5))
print(type(math.modf(1.2)))

#copysign()将第二个书的符号(正负号)传给第一个数   返回第一个数值的浮点数
print(math.copysign(4,-10))

#可以打印π和自然对数e的值
print(math.e)
print(math.pi)






import random
#random.random()  随机[0,1)的小数
print(math.ceil(random.random()))

#random.randint()  随机2个参数之间的整数   第一个参数我开始 第二个参数为结尾   可取到开头和结尾
print(random.randint(1,3))

#random.randrange()获取指定开始和结束之间的值  可指定间隔值  取不到结尾
print(random.randrange(1,3,step = 2))

# choice()随机获取列表中的值  (可迭代) 集合不能用
list1 = [5,2,0]
tuple1 = (4,6,)
set1 = {1,2,3}
print(random.choice(list1))
print(random.choice(tuple1))

# shuffle()随机打乱序列
random.shuffle(list1)
print(list1)

# uniform()随机获取指定 开始和结束的值   返回值为浮点数
print(random.uniform(1,5))
