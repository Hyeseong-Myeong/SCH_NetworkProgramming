from socket import *
import random

PORT = 2501
BUFSIZE = 1024

s = s = create_server(('', PORT), family=AF_INET, backlog=1)
conn, (remotehost, remoteport) = s.accept()
print("connected by ", remotehost, remoteport)

#Request 메시지 수신 시 심박수 걸음수 소모 칼로리 전송
while True :
    data = conn.recv(BUFSIZE)
    if not data:
        break

#심박수 40~140, 걸음수 2000~6000, 소모 칼로리 1000~4000
    data = data.decode()
    if data == "Request" :
        heartbeat = random.randrange(40,140)
        steps = random.randrange(2000,6000)
        cal = random.randrange(1000,4000)
#전송은 한번에 해도 되고, 따로 해도 됨.
#문자열, 정수(엔디언 고려) 중 택1.
        conn.send(f"Heartbeat={heartbeat} Steps={steps} Cal={cal}".encode())
        print(f"데이터 전송{heartbeat}, {steps},{cal}")
#quit 메시지 수신 시 종료
    elif data == "quit":
        conn.close()
        break