import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#서버는 소켓을 특정 (주소, 포트) 에 바인드시켜야 함
#주소를 작성하지 않을 경우, 내 컴퓨터의 모든 IP에 바인딩 함.(모든 인터넷 Interface, 가상머신 등)
#well known port를 피하기 위해 2000번 이후의 포트 사용 권장.
s.bind(('', 9000))
#listen(backlog) => backlog는 동시 연결 가능한 소켓 수를 의미
s.listen(2)

while True :
    #새로운 연결을 허용하기 위해 accept() 메소드 호출
    #s: 클라이언트의 연결을 기다리기 위한 소켓
    #client: 클라이언트와 통신하기 위한 소켓
    #addr: 연결된 client의 IP, Port 정보
    client, addr = s.accept()
    print("Connection from ", addr)
    client.send(b'Hello ' + addr[0].encode())
    client.close()