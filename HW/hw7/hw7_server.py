from socket import *
import threading
import time

port = 3333
BUFFSIZE = 1024

clients = []
addr = ('', port)

s = socket(AF_INET, SOCK_STREAM)
s.bind(addr)
s.listen(6)

print('Server started')

def client_chat(conn, addr):
    
    if(conn,addr) not in clients:
        print('new client', addr)
        clients.append((conn, addr))

    while True:
        data = conn.recv(BUFFSIZE)
        
        if not data:
            break;
        
        if 'quit' in data.decode():
            clients.remove((conn, addr))
            print('exit: ', addr)
            continue

        print(time.asctime() + str(addr) + " : " + data.decode())   

        for client in clients:
            if client[1] != addr:
                client[0].send(data)

while True:
    conn, addr = s.accept()
    print('connected by', addr)
    th = threading.Thread(target=client_chat, args=(conn,addr))
    th.start()
