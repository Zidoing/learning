import socket

sk = socket.socket()

address = ('127.0.0.1', 9000)

sk.bind(address)

sk.listen(3)

conn, address = sk.accept()
conn.send('yuea')


print conn.recv(1024)
print conn
