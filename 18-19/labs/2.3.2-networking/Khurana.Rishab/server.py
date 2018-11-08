import socket
class server:
	socket = socket.socket()
	host = "localhost"
	port = 3341
	socket.bind((host, port))
	socket.listen(5)
	while True:
		connection,addr = socket.accept()
		message = connection.recv(1024)
		print(message)
		connection.close()