with open('image.txt', 'r', encoding='utf8') as f:
    path = f.readline()
    path1 = f.readline()

print(path)
# path[0]到底是什么?
print(path[0] == ' ')
