from socket import *
import random
from collections import deque

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
chat = dict()

while True:
    data, addr = sock.recvfrom(BUFF_SIZE)
    msg = data.decode().split()

    if msg[0] == "send":
        mboxID = msg[1]     # mboxID 분리
        tmp = msg[2:]
        message = ' '.join(tmp) # message 분리
        
        if mboxID not in chat:  # chat 딕셔너리에 mboxID가 없을 경우
            chat[mboxID] = deque([message])
        else:
            chat[mboxID].append(message)
        sock.sendto(b"OK", addr)
        print("mboxID: {}, message: {}".format(mboxID, message))


    elif msg[0] == "receive":
        mboxID = msg[1]     # mboxID 분리

        if mboxID not in chat:  # chat 딕셔너리에 mboxID가 없을 경우
            sock.sendto(b"No messages", addr)
            print("No mboxID({}) or No messages".format(mboxID))

        else:
            if len(chat[mboxID]):   # 1개 이상있으면
                sock.sendto(chat[mboxID].popleft().encode(), addr)
            else:
                sock.sendto(b"No messages", addr)

    elif msg[0] == "quit":  # "quit" 수신 시 프로그램 종료
        break