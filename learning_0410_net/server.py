import socket
from threading import Thread, Lock

BUFFER_SIZE = 1024


def send():
    while True:
        if lock2.acquire():
            data = input('请输入要回复的数据: ')
            server.sendto(data.encode('utf8'), recv_data[1])


def recv():
    while True:
        global recv_data
        lock1.acquire()
        recv_data = server.recvfrom(BUFFER_SIZE)
        recv_data = (recv_data[0].decode(encoding='gbk'), recv_data[1])
        print('\n消息: %s, 来自: %s' % recv_data)
        lock1.release()
        lock2.release()


def main():
    send_thread = Thread(target=send)
    send_thread.start()
    recv_thread = Thread(target=recv)
    recv_thread.start()

    send_thread.join()
    recv_thread.join()
    server.close()
    print('finish')


if __name__ == '__main__':
    # 创建一个网络传输的UDP服务器
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 设置服务器地址和端口
    server.bind(('192.168.12.149', 50000))
    recv_data = None
    # 创建锁
    lock1 = Lock()
    lock2 = Lock()
    lock2.acquire()
    main()
