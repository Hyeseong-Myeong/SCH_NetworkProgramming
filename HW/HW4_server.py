from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)

    while True:
        data = client.recv(1024)
        
        if not data:
            break
        
        try:
            exp = data.decode()
            exp.replace(" ", "")
            num1 = ""
            num2 = ""
            
            while exp[0] >= "0" and exp[0] <= "9" :
                num1 = num1 + exp[0]
                exp = exp[1:]  

            op = exp[0]
            num1 = int(num1)
            num2 = int(exp[1:])

            if op == '+' :
                ans = num1 + num2
            elif op == '-' :
                ans = num1 - num2
            elif op == '*' :
                ans = num1 * num2
            elif op == '/' :
                ans = num1/num2

            ans = round(ans, 0)
            ans = str(ans)
        
        except:
            client.send(b'Try again')
        else:
            client.send(ans.encode())

    client.close()