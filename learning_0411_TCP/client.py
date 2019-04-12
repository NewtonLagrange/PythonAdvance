"""
TCP client
"""
import socket
from threading import Thread

ADDR = ('192.168.12.149', 60000)
BUFFER_SIZE = 1024


def login(fun):
    def login_():
        username = input('请输入你的用户名: ').encode('utf8')
        client.send(username)
        while True:
            print('##################################')
            print('\t\t 聊天类型')
            print('\t\t 1. 群聊')
            print('\t\t 2. 私聊')
            chat_type = input('请输入聊天类型编号: ')
            print(chat_type)
            if chat_type == '1' or chat_type == '2':
                client.send(chat_type.encode('utf8'))
                break
            else:
                print('无效选项, 请重新输入.......')

        fun()

    return login_


def recv():
    """ 接受服务器消息 """
    while True:
        # TODO 服务器断开时会报错
        data = client.recv(BUFFER_SIZE)
        if len(data):
            print('\n', data.decode('utf8'))
        else:
            print('\n服务器切断连接......')
            client.close()
            break


@login
def send():
    """ 发送消息给服务器 """
    while True:
        data = input('请输入发送的消息(私聊格式: username: content): ').encode('utf8')
        try:
            client.send(data)
        except Exception as e:
            print('\n', e)
            break


def main():
    """  """
    recv_thread = Thread(target=recv)
    send_thread = Thread(target=send)
    recv_thread.start()
    send_thread.start()

    recv_thread.join()
    send_thread.join()


if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    main()
