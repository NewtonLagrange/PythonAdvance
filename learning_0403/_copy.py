import copy

# 赋值和copy的区别
# 对于可变数据类型: 赋值之后两个变量名指向同一个内存地址, copy之后两个变量名指向不同内存地址
n1 = [1, 2]
n2 = n1
# 赋值
print(n1 is n2)
n3 = copy.copy(n1)
print(n1 is n3)

# 对于不变数据类型: 赋值之后两个变量名指向同一个内存地址, copy之后两个变量名指向相同同内存地址
print('2 ########################')
tu1 = (1, [1, 2])
tu2 = tu1
tu3 = copy.copy(tu1)
print(tu1 is tu2)
print(tu1 is tu3)

# 浅拷贝和深拷贝的区别
# 浅拷贝之后变量内部嵌套的数据内存地址相同, 而深拷贝则不同
print('3 #########################')
t1 = [1, [1]]
t2 = copy.copy(t1)
t3 = copy.deepcopy(t1)
print(t1[1] is t2[1])
print(t1[1] is t3[1])
