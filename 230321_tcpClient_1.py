import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
#addr 주소의 서버로 접속
sock.connect(addr)
#최대 1024바이트의 데이터를 읽어와서 반환
msg = sock.recv(1024)
#수신한 데이터를 문자열 처리하기위해 decode()메소드 사용
print(msg.decode())

sock.close()