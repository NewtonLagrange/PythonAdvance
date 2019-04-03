from sys import getrefcount

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list1.append(list2)
list2.append(list1)
list3 = list1
print(getrefcount(list1))
del list2
print(getrefcount(list1))
n = 1
print(getrefcount(n))
id()
