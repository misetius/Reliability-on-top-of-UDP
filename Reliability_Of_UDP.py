import socket
import random


class Virtuaalisoketti:
    def __init__(self, portti, ip, todennakoisyys = 0.5):
        self.soketti = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.soketti.bind((ip, portti))

    def receivedata(self):
        while True:
            data, addr = self.soketti.recvfrom(1024)
            return data




portti = 6666
ip = "127.0.0.1"

omasoketti = Virtuaalisoketti(portti, ip)

kuunnellaan = True
while kuunnellaan:
    print(omasoketti.receivedata())
    

