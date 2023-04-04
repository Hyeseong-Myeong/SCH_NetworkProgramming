import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)

sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())
sock.send("Myeong Hyeseong".encode())
print(sock.recv(1024).decode())

sock.close()