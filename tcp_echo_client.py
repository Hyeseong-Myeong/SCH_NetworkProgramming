import socket

# 클라이언트 실행
host = 'localhost'  # 서버 호스트 이름
port = 2500      # 서버 포트 번호


def tcp_echo_client(host, port):
    # TCP 소켓 생성
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # 서버에 연결
        sock.connect((host, port))
        print(f"Connected to {host}:{port}")

        while True:
            # 사용자로부터 입력 받기
            message = input("Enter a message to send (or 'q' to quit): ")

            if message == 'q':
                break

            # 메시지 서버로 전송
            sock.sendall(message.encode())

            # 서버로부터 응답 받기
            data = sock.recv(1024)
            print("Received:", data.decode())

    finally:
        # 소켓 종료
        sock.close()
        print("Connection closed.")

tcp_echo_client(host, port)