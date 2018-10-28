#　TCP客户端
from socket import *

# 服务器的地址
HOST = "localhost"
PORT = 21565
BUFSIZ = 1024
ADDR = (HOST, PORT)

# 创建客户端套接字并和服务器进行连接
tcpClientSock = socket(AF_INET, SOCK_STREAM)
tcpClientSock.connect(ADDR)

while True:
	data = input(">>>")
	if not data:
		break
	tcpClientSock.send(data.encode())
	data_back = tcpClientSock.recv(BUFSIZ).decode()
	if not data_back:
		break
	print("Server {}:{}".format(ADDR, data_back))

tcpClientSock.close()
print("客户端套接字已删除！") 