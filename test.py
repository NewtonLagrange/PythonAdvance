import requests

with open('image.txt', 'r', encoding='utf8') as f:
    path = f.readline()

print(path)