import socket
import sys

tcp_port = 66 # Insert a Free Port as per your choice
tcp_ip = '0.0.0.0'
buf_size = 30
msg = "Connected Successfully"
msg = msg.encode('utf-8')

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket successfully created")

s.bind((tcp_ip,tcp_port))
print("Socket is binded to",tcp_port)

s.listen(1)
print("Socket is listening")

c,addr = s.accept()
print("Connection address from",addr)

data = c.recv(buf_size)
data = data.decode('utf-8')

print("Received Data from client : ",data)
c.send(msg)

c.close()
