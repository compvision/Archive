import socket

sock = socket.socket()
port = 3341
host = "localhost"
sock.bind((host,port))
sock.listen(5)

while True:
    conn, addr = sock.accept()
    print(addr[0])
    message = conn.recv(1024)
    msg = message.decode("utf-8")
    print(msg)
    if ("Hello" in  msg):
        print("hi")
    else:
        print("bye")
