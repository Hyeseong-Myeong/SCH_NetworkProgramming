from socket import *
import threading

port = 3333
BUFFSIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
addr = ('localhost', port)
s.connect(addr)

def handler(sock):
    while True:
        data = sock.recv(BUFFSIZE)
        if not data:
            break

        print(data.decode())

uid = input("input ID: ")
s.send(('['+uid+']').encode())

th = threading.Thread(target=handler, args = (s, ))
th.daemon = True
th.start()

while True:
    data = '[' + uid + '] ' + input()
    s.send(data.encode())
