from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 6666
ADDR = (HOST,PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)

while True:
    viesti = input("> ")
    
    udpCliSock.sendto(viesti.encode(),ADDR) 
    
    
    recv_data,ADDR = udpCliSock.recvfrom(1024)
    
        
    

