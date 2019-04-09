from multiprocessing import Process
import requests
# 创建32个进程去分别下载32张图片


def read():
    with open('image.txt', 'r', encoding='utf8') as f:
        i = 1
        for path in f:
            path1 = path.strip()
            print(path1)
            if i != 1:
                response = requests.get(path1)
                with open('./images1/img_%s.jpg' % i, 'wb') as file:
                    file.write(response.content)

            i += 1


def main():
    for i in range(4):
        read_p = Process(target=read)
        read_p.start()

    read_p.join()
    print('finish')


if __name__ == '__main__':
    main()
