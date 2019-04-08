import copy

# 赋值的浅拷贝的区别
# 对于可变数据类型, 赋值之后两个变量指向同一个地址, 浅拷贝之后两个变量指向不同的地址(即浅拷贝新建引用指针)
a = [1, 2, 3]
b = a
c = copy.copy(a)
print(a is b)
print(a is c)
# 对于不可变数据类型, 赋值, 浅拷贝和深拷贝效果一样, 不同变量名指向同一个内存地址,
a = (1, 2, 3)
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
print(a is b)
print(a is c)
print(a is d)

print('###########################################')
# 对于不变数据类型, 浅拷贝和深拷贝没有区别(包含可变类型嵌套不变类型)
# 最终比较不变数据类型, 浅拷贝和深拷贝没有区别
a = [1, (1, 2)]
b = copy.copy(a)
c = copy.deepcopy(a)
print(a[1] is b[1])
print(a[1] is c[1])

# 最终可变数据类型, 浅拷贝只对外层新建引用指针, 而深拷贝对外层和多有里层新建指针
a = [1, [1, 2]]
b = copy.copy(a)
c = copy.deepcopy(a)
print(a[1] is b[1])
print(a[1] is c[1])
