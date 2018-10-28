# coding:utf8
# 创建一个TCP服务器，接受用户发来的字符串，添加一个时间戳后返回给客户端
from socket import *
from datetime import datetime

HOST = ""
PORT = 21565
BUFSIZ = 1024 # 设置缓冲区大小为1K
ADDR = (HOST, PORT)


# TCP服务器创建套接字   (socket_family, socket_type)
tcpServerSock = socket(AF_INET, SOCK_STREAM) 
# 把套接字绑定到固定地址
tcpServerSock.bind(ADDR)
# 服务器同时最多接受5个链接
tcpServerSock.listen(5)


while True:
	print("正在等待连接........")
	# 服务器套接字在端口等待连接，否则一直等待
	tcpClientSock, addr = tcpServerSock.accept()
	print("connected from:", addr)

	while True:
		# 要对接收到的data进行解码，对发送的data进行编码
		data = tcpClientSock.recv(BUFSIZ).decode()
		if not data:
			break
		print("Client {}:{}".format(ADDR, data))
		tcpClientSock.send(("{}:{}".format(datetime.now(), data)).encode())
	tcpClientSock.close()

tcpServerSock.close()