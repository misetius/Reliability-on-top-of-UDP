import socket
import random
import time

class Virtuaalisoketti:
    def __init__(self, portti, ip):
        self.soketti = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.soketti.bind((ip, portti))
    
    #soketti valmis ottamaan dataa
    def receivedata(self):
        while True:
            data, addr = self.soketti.recvfrom(1024)
            r3 = random.randint(0, 100)
    
            dekoodattu_data = data.decode('utf-8')
            
            pariteetti = dekoodattu_data[-1]
            sisalto = dekoodattu_data[:-1]

            #lisätään bittivirhe jos r3 muuttujan tulos alle tai yhtä kuin 50
            if r3 <= 50:
                mahdollisestivirheellinenviesti = bittivirheenlisaaminen(sisalto)
                print(mahdollisestivirheellinenviesti)
                
            else:
                print(sisalto)
                mahdollisestivirheellinenviesti = sisalto

            

            pariteetintarkistus = laskepariteetti(mahdollisestivirheellinenviesti)

            if pariteetti == pariteetintarkistus:
                palautus = "ACK"
                self.soketti.sendto(palautus.encode(), addr)
            





            
                

def bittivirheenlisaaminen(viesti):
    binaarilista = []

    for merkki in viesti:
        binaarilista.append(bin(ord(merkki))[2:].zfill(8))

    binaarilista = ''.join(binaarilista)
    binaarilista = list(binaarilista)
    r4 = random.randint(0, len(binaarilista)-1)
    muutettavabitti = binaarilista[r4]
    if muutettavabitti == '1':
        binaarilista[r4] = '0'
    else: 
        binaarilista[r4] = '1'
    
    binaariluku = ''.join(binaarilista)
    

    binaariviestiksi = ""

    for i in range(0, len(binaariluku), 8):
        binc = binaariluku[i:i + 8]
        num = int(binc, 2)
        binaariviestiksi += chr(num)
    return binaariviestiksi


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



portti = 6666
ip = "127.0.0.1"

omasoketti = Virtuaalisoketti(portti, ip)

omasoketti.receivedata()
    

