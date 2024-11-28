import socket
import random
import time

class Virtuaalisoketti:
    def __init__(self, portti, ip):
        self.soketti = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.soketti.bind((ip, portti))

    def receivedata(self):
        while True:
            data, addr = self.soketti.recvfrom(1024)
            r1 = random.randint(0, 100)
            r2 = random.randint(0, 100)
            r3 = random.randint(0, 100)

            if r1 < 50 and r2<50:
                data = data[0:-1]
                dekoodattu_data = data.decode('utf-8')
                if r3 < 50:
                    dekoodattu_data = bittivirheenlisaaminen(dekoodattu_data)
                print(dekoodattu_data)

            elif r1<50 and r2 > 50:
                data = data[0:-1]
                dekoodattu_data = data.decode('utf-8')
                if r3 < 50:
                    dekoodattu_data = bittivirheenlisaaminen(dekoodattu_data)
                time.sleep(1)
                print(dekoodattu_data)

#011011010110111101101001 = moi
            else:
                print("Dropped packet")
                

def bittivirheenlisaaminen(viesti):
    binaarilista = []

    for merkki in viesti:
        binaarilista.append(bin(ord(merkki))[2:].zfill(8))

    

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

    



portti = 6666
ip = "127.0.0.1"

omasoketti = Virtuaalisoketti(portti, ip)

omasoketti.receivedata()
    

