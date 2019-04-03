import builtins
from sys import getrefcount

count = getrefcount([1, 2])
print(count)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.append(list2)
list2.append(list1)
print(id(list1), id([1, 2, 3]))

print(getrefcount([1, 2, 3]))
del list1
del list2
print(getrefcount([1, 2, 3]))
print(dir(builtins))
