import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname() # Substitute for IP locally.
PORT = 5000

s.connect((HOST_NAME, PORT))
# 100 is buffer size, those messages need to be accepted in chunks.
msg = s.recv(100)
print(msg.decode('utf-8')) # decoding the message.