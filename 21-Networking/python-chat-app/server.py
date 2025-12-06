# Importing libraries.
import socket
from tkinter import *

# Send Functionality Of App
def send(listbox,entry):
    message = entry.get() # Getting input.
    listbox.insert(END, "Server: " +  message)
    entry.delete(0, END) # After sending the message we delete the input
    client.send(bytes(message, "utf-8")) # Sending message to client.

# Receive Functionality Of App
def receive(listbox):
    message_from_client = client.recv(50) # Receiving message from client
    listbox.insert(END, "Client: " + message_from_client.decode('utf-8')) # Decode message.

root = Tk() # Initialize tkinter.
root.minsize(200,200)
entry = Entry() # Entry to input the message.
entry.pack(side=BOTTOM)

# To display the messages.
listbox = Listbox(root)
listbox.pack()

# Buttons to send and receive messages.
button = Button(root, text="Send", command=lambda: send(listbox,entry))
button.pack(side=BOTTOM)

rbutton = Button(root, text="Recieve", command=lambda: receive(listbox))
rbutton.pack(side=BOTTOM)

root.title("Server") # Title at the top.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Establishing socket.

# Host, Port and binding it.
HOST_NAME = socket.gethostname()
PORT = 9999
s.bind((HOST_NAME, PORT))

# Listening to client.
s.listen(10)
client, address = s.accept()

root.mainloop() # Tkinter loop end.