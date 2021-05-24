import socket

tcp_port = 79
tcp_ip = '127.0.0.1'
buf_size = 30

print("[INFO] Creating Socket...")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("[INFO] Socket successfully created")

print("[INFO] Connecting Socket to port",tcp_port)
s.connect((tcp_ip,tcp_port))
print("[INFO] Socket connected successfully to port",tcp_port)

msg = "Hello Cruel World"
print("[INFO] Encoding data...")
msg = msg.encode('utf-8')

print("[INFO] Sending data to Server...")
s.send(msg)
print("[INFO] Data sent successfully to Server")

print("[INFO] Receiving Data from server")
data = s.recv(buf_size)

print("[INFO] Decoding received data...")
data = data.decode('utf-8')

print('[INFO] Data received from Server : ',data)

print("[INFO] Disconnecting Socket...")
s.close()
print("[INFO] Socket disconnected successfully")