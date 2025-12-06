import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


HOST_NAME = socket.gethostname()
PORT = 5000
s.bind((HOST_NAME, PORT))
s.listen(4)

while True:
    client, address = s.accept() # Request accepting from client
    client.send(bytes("Hey there, what's up?", "utf-8")) # Trying to send a client a message.
    print(address)
    client.close()
