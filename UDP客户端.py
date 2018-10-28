#coding:utf8
from socket import *


udpClientSock = socket(AF_INET, SOCK_DGRAM)

while True:
	data = input(">>>")
	if not data:
		break
	udpClientSock.sendto(data.encode(), ("localhost",21567))
	data, addr = udpClientSock.recvfrom(1024)
	if not data:
		break
	print("UDPServer {}:{}".format(addr, data.decode()))

udpClientSock.close()