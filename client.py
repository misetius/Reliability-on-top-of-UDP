from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 6666
ADDR = (HOST,PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)

while True:
    viesti = input("> ")
    viestidekoodattuna = b"{viesti}"
    udpCliSock.sendto(viesti.encode(),ADDR) 
    
    
    #recv_data,ADDR = udpCliSock.recvfrom(BUFSIZE)
    #if recv_data is not None:
     #  print "[%s]: receiving data from server %s:%s  :%s" %(ctime(),ADDR[0],ADDR[1],recv_data)
    
udpCliSock.close()
