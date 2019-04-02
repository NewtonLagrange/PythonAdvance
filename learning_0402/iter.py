"""
判断常用数据类型是否 Iterable 和 Iterator
"""

from collections.abc import Iterable, Iterator
d = {'name': 'outime', 'age': 21}
li = [1, 2, 3, 4, 5]
t = (1, 2, 3, 4, 5)
s = 'outime'
num = 10000
test_set = {1, 2, 3, 4, 5}
print('以下类型是否Iterable')
print('dict:', isinstance(d, Iterable))
print('list:', isinstance(li, Iterable))
print('tuple:', isinstance(t, Iterable))
print('string:', isinstance(s, Iterable))
print('int:', isinstance(num, Iterable))
print('set:', isinstance(test_set, Iterable))

print('以下类型是否是Iterator')
print('dict:', isinstance(d, Iterator))
print('list:', isinstance(li, Iterator))
print('tuple:', isinstance(t, Iterator))
print('string:', isinstance(s, Iterator))
print('int:', isinstance(num, Iterator))
print('set:', isinstance(test_set, Iterator))


