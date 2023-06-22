import socket

target_host  ="172.27.144.1"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.sendto("ABCDEF",(target_host, target_port))

data, addr = client.recvfrom(4096)
print(data)