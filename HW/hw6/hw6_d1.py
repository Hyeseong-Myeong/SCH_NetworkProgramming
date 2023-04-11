#디바이스 1 : 온도 습도 조도 제공
from socket import *
import random

PORT = 2500
BUFSIZE = 1024

s = create_server(('', PORT), family=AF_INET, backlog=1)
conn, (remotehost, remoteport) = s.accept()
print("connected by ", remotehost, remoteport)

#사용자로부터 Request 메시지 수신시 전송
while True :
    data = conn.recv(BUFSIZE)
    if not data:
        break

#온도: 0~40 습도 0~100 조도70~150
    data = data.decode()
    if data == "Request" :
        temp = random.randrange(0,40)
        humid = random.randrange(0,100)
        iilum = random.randrange(70,150)
#전송은 한번에 해도 되고, 따로 해도 됨.
#문자열, 정수(엔디언 고려) 중 택1.
        conn.send(f"Temp={temp} Humid={humid} Iilum={iilum}".encode())
        print(f"데이터 전송 완료{temp}, {humid}, {iilum}")
#quit 메시지 수신 시 종료
    elif data == "quit":
        conn.close()
        break