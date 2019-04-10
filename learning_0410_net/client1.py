"""
UDP协议客户端
"""
import socket
from threading import Thread

IP_PORT = ('192.168.12.149', 50000)
BUFFER_SIZE = 1024
# socket.AF_INET: 表示网络间传输, socket.SOCK_DGRAM: 表示UDP协议
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send():
    while True:
        data = input('请输入要发送的数据: ')
        client.sendto(data.encode('utf8'), IP_PORT)


def recv():
    while True:
        recv_data = client.recvfrom(BUFFER_SIZE)
        recv_data = (recv_data[0].decode(encoding='utf8'), recv_data[1])
        print('\n消息: %s, 来自: %s' % recv_data)


def main():
    client.sendto('hello'.encode('utf8'), IP_PORT)
    send_p = Thread(target=send)
    send_p.start()
    recv_p = Thread(target=recv)
    recv_p.start()

    send_p.join()
    recv_p.join()
    client.close()
    print('finish')


if __name__ == '__main__':
    main()
