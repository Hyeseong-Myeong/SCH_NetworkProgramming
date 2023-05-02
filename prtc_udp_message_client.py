from socket import *

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter the message("send [mboxID] message" or "receive mboxID"): ')
    sock.sendto(msg.encode(), ('localhost', port))

    if msg == 'quit':   # "quit" 입력 시 프로그램 종료
        break

    data, addr = sock.recvfrom(BUFF_SIZE)
    print(data.decode())

sock.close()