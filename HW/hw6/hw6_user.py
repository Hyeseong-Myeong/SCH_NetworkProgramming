import socket
import datetime

#2개의 디바이스와 TCP 연결
BUF_SIZE = 1024
D1_PORT = 2500
D2_PORT = 2501
FILENAME = "data.txt"

s1 = socket.create_connection(('localhost', D1_PORT))
s2 = socket.create_connection(('localhost', D2_PORT))
    
#데이터 저장 함수 구현
def saveData(data) :
    try:
        f = open(FILENAME, 'a')

    except FileNotFoundError:
        print("파일이 존재하지 않습니다.")
    
#Fri Mar 11 22:55:13 2023: Device1: Temp=20, Humid=50, Iilum=100
    else:
        data = datetime.datetime.now().strftime("%a %b %d %H:%M:%S 20%y: ") + "Device" + input_msg + ": " + data
        f.write(data + "\n")


#1 입력시 디바이스 1에 Request 전송
#2 " 디바이스 2에 "
while True :
    input_msg = input("명령어를 입력해주세요")

    if input_msg == "1" :
        s1.send("Request".encode())

    elif input_msg == "2" :
        s2.send("Request".encode())

#quit 입력 시 디바이스에 quit 전송 후 종료    
    elif input_msg == "quit" :
        s1.send("quit".encode())
        s2.send("quit".encode())
        s1.close()
        s2.close()
        break

    print("전송완료")

#수집한 데이터는 시간정보 추가하여 data.txt에 저장

    while True:
        if input_msg == "1":
            d1_data = s1.recv(BUF_SIZE)
            data = d1_data.decode()

        elif input_msg == "2":
            d2_data = s2.recv(BUF_SIZE)
            data = d2_data.decode()

        print(f"수신 데이터: {data}")    

        saveData(data)
        print("데이터를 저장했습니다.")
        break;
