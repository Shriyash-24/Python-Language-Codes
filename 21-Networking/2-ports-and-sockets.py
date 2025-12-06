# Port - A port is communication endpoint.
# IP address isn't enough, you also need to specify the port to which you want to connect to.
# Each device has multiple ports, each port has a different purpose.
# If IP is like your residential address, port number is like your apartment.
# To connect to srver over a network, you also need it's port number.
# IP states which server you want to connect to, port states at what location on server you want to connect to.

# FTP - 20
# FTP Command Control - 21
# SSH - 22
# HTTP - 80
# HTTPS - 443
# SMTP - 25

# Socket - It is an endpoint in communication flow between 2 programs running over network.
# They allow communication between 2 different processes running on same or different machines.
# Socket Address = IP Address + Port Number.
# Acts as a layer of communication between 2 computers.
# Client (Port 80) --> SOCKET --> Server (Port 80)

# Why are sockets required?
# 1. Let's say I want a send a message from 1 computer to another.
# 2. I would need an IP address of other computer.
# 3. I would also need a port of other computer which accepts a message.
# 4. Once we have IP and Port number, we need to establish a connection.
# 5. This connection can be established via socket.

# 1. Create a socket for communication.
# 2. Bind the socket with the IP address and the port number of the reciever.
# 3. Send a message via socket.
