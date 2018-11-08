import socket

soc = socket.socket()
soc.bind(("localhost", 3341))
print("starting")
soc.listen(5)
while True:
	conn, addr = soc.accept()
	print(conn.recv(1024))
	conn.close()