# coding:utf8
from socket import *
from datetime import datetime

HOST = ""
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpServerSock = socket(AF_INET, SOCK_DGRAM)
udpServerSock.bind(ADDR)

while True:
	print("等待接受....")
	data, addr = udpServerSock.recvfrom(BUFSIZ)
	udpServerSock.sendto(("{}:{}".format(datetime.now(), data.decode()).encode()), addr)
	print("returned to:", addr)

udpServerSock.close()