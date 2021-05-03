import socket

tcp_port = 66 # Insert a Free Port as per your choice
tcp_ip = 'xx.xx.xx.xx' # Insert IP Address
buf_size = 30
msg = "Hello World"
msg = msg.encode('utf-8')

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket successfully created")

s.connect((tcp_ip,tcp_port))
print("Socket is connected to",tcp_port)

s.send(msg)
data = s.recv(buf_size)
data = data.decode('utf-8')

print('Data received from Server : ',data)
s.close()
