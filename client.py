from socket import *
from time import ctime

def laskepariteetti(viesti):
    binaarilista = []
    
    for merkki in viesti:
        binaarilista.append(bin(ord(merkki))[2:].zfill(8))

    binaarilista = ''.join(binaarilista)
    binaarilista = list(binaarilista)
    pariteettibitti = int(binaarilista[0]) ^ int(binaarilista[1])


    for i in range(2, len(binaarilista)):
        pariteettibitti = pariteettibitti ^ int(binaarilista[i])

    return str(pariteettibitti)

HOST = '127.0.0.1'
PORT = 6666
ADDR = (HOST,PORT)

udpsoketti = socket(AF_INET,SOCK_DGRAM)

while True:
    viesti = input("> ")
    pariteetti = laskepariteetti(viesti)
    viesti = viesti+pariteetti
    udpsoketti.sendto(viesti.encode(),ADDR) 
    
    while True:
            try:
                udpsoketti.settimeout(3)
                recv_data,ADDR = udpsoketti.recvfrom(1024)

                dekookattu_data = recv_data.decode('utf-8')

       
                if dekookattu_data == "ACK":
                    print("Palvelin vastaanotti viestin onnistuneesti")
                    break
                elif dekookattu_data == "NACK":
                    print("Palvelimen vastaanottamassa paketissa oli virhe")
                    udpsoketti.sendto(viesti.encode(),ADDR)

            except timeout:
                print("Palvelin ei vastannut ajoissa")
                udpsoketti.sendto(viesti.encode(),ADDR)

    
        
    

