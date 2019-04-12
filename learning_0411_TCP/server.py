"""
TCP server
"""
import socket
from threading import Thread, Lock

ADDR = ('192.168.12.149', 60000)
BUFFER_SIZE = 1024


def acc():
    """ 接受客户端连接 """
    while True:
        client, client_addr = server.accept()
        # 给当前用户创建一个连接线程
        client_thread = Thread(target=recv, args=(client, ))
        client_thread.start()


def recv(client):
    """ 接收客户端消息 """
    client_name, chat_type = add_user(client)
    if not client_name:
        # 防止用户在不输入用户名直接关闭连接
        return client.close()

    while True:
        try:
            recv_send(client, client_name, chat_type)
        except Exception as e:
            print(e, '行号: 29')
            break


def recv_send(client, client_name, char_type):
    """ 接受并发送消息 """
    data = client.recv(BUFFER_SIZE).decode('utf8')
    if len(data):

        if char_type == '1':
            group_chat(data, client_name)
        else:
            username, info = data.split(':')

            if username in clients.keys():
                data = '消息来自: %s, 内容: %s' % (client_name, info)
                clients[username].send(data.encode('utf8'))
            else:
                # TODO 将数据保存下来等到用户上线的时候发过去
                data = '用户: %s, 已离线.....'.encode('utf8') % client.getpeername()[1]
                client.send(data)

    else:
        clients.pop(client.getpeername()[1])
        return client.close()


def group_chat(data, client_name):
    """ 群聊 """
    data = '消息来自: %s, 内容: %s' % (client_name, data)
    for client in clients:

        if client == client_name:
            pass
        else:
            clients[client].send(data.encode('utf8'))


def add_user(client):
    """
        添加用户名到 clients.
        将字典clients中的 port 键改为 username.
     """
    try:
        username = client.recv(BUFFER_SIZE).decode('utf8')
        clients[username] = client
        chat_type = client.recv(BUFFER_SIZE).decode('utf8')
        print('\n来了一个新用户: %s, 用户数量: %s' % (username, len(clients)))
        return username, chat_type
    except Exception as e:
        print(e)
        return False, False


def main():
    acc_thread = Thread(target=acc)
    acc_thread.start()

    acc_thread.join()

    # recv()
    # send()
    for client in clients:
        client[0].close()
    print(11111111)
    server.close()
    print('finish')


if __name__ == '__main__':
    # 建立服务器 socket对象
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置客户端对象列表
    clients = dict()
    # 设置服务器地址
    server.bind(ADDR)
    # 启动监听
    server.listen(10)
    print('服务器: %s. 正在等待连接中......' % (ADDR, ))
    # 创建一把锁
    lock = Lock()
    lock.acquire()
    main()
