import socket
from multiprocessing import Process
IP_PORT = ('192.168.12.149', 60000)
BUFFER_SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



data = input('请输入要发送的数据: ')

client.sendto(data.encode('utf8'), IP_PORT)



while True:
    recv_data = client.recvfrom(BUFFER_SIZE)
    print(recv_data)


