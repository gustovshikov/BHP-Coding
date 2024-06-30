import socket

target_host = "127.0.0.1"
target_port = 9998

# create socketobject
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

# send some data
client.send(b"AABBCC TEST")

# receive some data
response = client.recv(4096)

print(response.decode())
client.close()

