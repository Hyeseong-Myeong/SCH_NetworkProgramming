from socket import *

BUFFSIZE = 1024
port = 5555

sock = socket(AF_INET, SOCK_DGRAM)
#원래는 UDP는 connect 필요 없음
#프로그래밍 상 편의를 위해 보낼 때 마다 주소를 쓰지 않기위해 사용.
#꼭 connect 할 필요 없음
sock.connect(('localhost', port))

for i in range(10):
    time = 0.1
    data= 'Hello, IoT'
    while True:
        sock.send(data.encode())
        print('Packet({}): Waiting up to {} secs for ack'.format(i, time))
        sock.settimeout(time)
        
        try:
            data = sock.recv(BUFFSIZE)
        except timeout:
            time *= 2
            if time > 2.0:
                break
        else:
            print('Response', data.decode())
            break