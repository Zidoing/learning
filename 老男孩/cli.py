import socket

sk = socket.socket()

address = ('127.0.0.1', 9000)

sk.connect(address)

sk.send('nihao ')

print sk.recv(1024)

