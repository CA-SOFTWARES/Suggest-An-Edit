import socket
import sys
import time
s = socket.socket()
ho = socket.gethostname()
print("Server Will Start On Host:",ho)
host = input(str(">: "))
if host == ho:
    port = 1234
    try:
        s.connect((host, port))
        print("Connected To Host", ho,"And Server Is Now Online")
    except:
        print("Connection To Host Is Failed")
        w = input("")
    while 1:
        incoming = s.recv(1024)
        incoming = incoming.decode()
        print("Server:>>", incoming)
        message = input("You:>> ")
        message = message.encode()
        s.send(message)

else:
    print("Could Not Connnect Host Or You Entered Wrong Host Name")
    print("Please Restart The Programm")
    a = input("")