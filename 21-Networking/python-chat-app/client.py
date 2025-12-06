# Importing Libraries.
import socket
from tkinter import *

# Send Functionality Of Our App.
def send(listbox,entry):
    message = entry.get() # Getting input.
    listbox.insert(END, "Client: " + message) # Inserting it in our listbox.
    entry.delete(0, END) # Deleting the input box after delete.
    s.send(bytes(message.encode('utf-8'))) # Sending message.
    receive(listbox)

# Receive Functionality Of Our App.
def receive(listbox):
    message = s.recv(50)
    listbox.insert(END, "Server: " + message.decode('utf-8'))

root = Tk()
root.minsize(200,200)

# To input the message.
entry = Entry()
entry.pack(side=BOTTOM)

# To display the messages.
listbox = Listbox(root)
listbox.pack()


# Buttons to send and receive.
button = Button(root, text="Send", command=lambda: send(listbox,entry))
button.pack(side=BOTTOM)

rbutton = Button(root, text="Recieve", command=lambda: receive(listbox))
rbutton.pack(side=BOTTOM)

# Title.
root.title("Client")

# Establishing connection.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 9999
s.connect((HOST_NAME, PORT))

# Tkinter loop ends.
root.mainloop()
