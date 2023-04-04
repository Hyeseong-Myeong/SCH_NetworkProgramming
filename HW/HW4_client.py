from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    exp = input('Expression to send :')
    if exp == 'q':
        break

    s.send(exp.encode())
    print('Answer: ', s.recv(1024).decode())

s.close()