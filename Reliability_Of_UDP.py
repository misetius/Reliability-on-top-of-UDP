import socket
import random


class Virtuaalisoketti:
    def __init__(self, portti, ip):
        self.soketti = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.soketti.bind((ip, portti))

    def receivedata(self):
        while True:
            data, addr = self.soketti.recvfrom(1024)
            r1 = random.randint(0, 100)

            if r1 < 50:
                data = data[0:-1]
                dekoodattu_data = data.decode('ascii')
                print(dekoodattu_data)
                
            else:
                print("Dropped packet")
                continue




portti = 6666
ip = "127.0.0.1"

omasoketti = Virtuaalisoketti(portti, ip)

omasoketti.receivedata()
    

