from socket import *



#80 포트를 열고 웹 클라이언트 연결 대기
s = socket()
s.bind(('', 80))
s.listen(10)

#연결이 들어올 경우, HTTP Request 첫 번째 라인을 읽어들임
#요청 형식은 GET /index.html HTTP/1.1
while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

#파일 명을 파싱 후 /을 제거하여 파일 명 얻음
    filename = req[0].split()[1][1:]
#파일이 존재할 경우 파일을 오픈 후 파일에 대한 mimeType 설정
#파일이 존재하는 경우 HTTP Response 메시지를 생성하여 전송
    try:
        f = ''
        if filename == "index.html":
            f = open(filename, 'r', encoding='utf-8')
            mimeType = 'text/html'
            
        elif filename == "iot.png":
            f = open(filename, 'rb')
            mimeType = 'image/png'

        elif filename == "favicon.ico":
            f = open(filename, 'rb')
            mimeType = 'image/x-icon'
        else :
            raise FileNotFoundError()
        
        
        header = "HTTP/1.1 200 OK\r\n" + 'Content-type: ' + mimeType + '\r\n\r\n' 
        data = f.read()
        if filename == "index.html":
            c.send(header.encode('utf-8') + data.encode('euc-kr'))

        else:
            c.send(header.encode('utf-8') + data)



#파일이 존재하지 않는 경우 404 리턴
    except FileNotFoundError:
        header = "HTTP/1.1 404 Not Found\r\n\r\n<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>"
        body = "<BODY>Not Found</BODY></HTML>"
        c.send((header + body).encode('utf-8')) 
        print('존재하지 않는 파일명입니다.')

        c.close()

#파일이 존재하면 읽어서 전송
#헤더
#'HTTP/1.1 200 OK\r\n'
#'Content-type: ' + mimeType + '\r\n'
#'\r\n'
    else:
        c.close()
#바디는 파일을 읽어서 전송
#data = f.read()를 이용
#c.send(data.encode('euc-kr)) #index.html등 한글 텍스트
#c.send(data) #그 외 바이너리 파일

