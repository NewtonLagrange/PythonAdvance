import requests

with open('image.txt', 'r', encoding='utf8') as f:
    i = 1
    for path in f:
        path1 = path.strip()
        print(path1)
        if i != 1:
            response = requests.get(path1)
            with open('./images/img_%s.jpg' % i, 'wb') as file:
                file.write(response.content)

        i += 1
