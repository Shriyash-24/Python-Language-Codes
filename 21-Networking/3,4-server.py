import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2 parameters - Family type of sockets, Type of socket.
# AF_INET --> IPv4, AF_INET6 --> IPv6.
# AF - Address Family
# TCP Socket - SOCK_STREAM, uses stream of data.

HOST_NAME = socket.gethostname()
PORT = 5000
s.bind((HOST_NAME, PORT)) # We can pass these in a tuple.
s.listen(4) # Backlog...number of accepted connections.

while True:
    client, address = s.accept() # Request accepting from client
    client.send(bytes("Hey there, what's up?", "utf-8")) # Trying to send a client a message.
    print(address)
