from socket import *
import random

BUFFSIZE = 1024
port = 5555

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
print('Listening...')

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    if random.randint(1,10) <= 3:
        print('Packet from {} lost!'.format(addr))
        continue
    print("Packet is {} from {}".format(data.decode(), addr))

    sock.sendto('ack'.encode(), addr)  