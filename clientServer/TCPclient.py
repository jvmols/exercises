import socket
from datetime import datetime

target_host= "127.0.0.1"
target_port = 9999

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send("Time: "+str(datetime.now())+", \r\nMessage: Works?\r\n\r\n")

# receive some data
response = client.recv(4096)

print response