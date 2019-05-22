from time import localtime, strftime
import socket

print("The server has started successfull..\nPort: 9090")

sock = socket.socket()
sock.bind(('', 9090))
sock.listen()
conn, addr = sock.accept()

print('\nСonnected:', addr)

while True:
	data = conn.recv(1024).decode()
	if data.lower() == "y":
		conn.send(strftime("%d.%m.%Y %H:%M:%S", localtime()).encode())
	elif data.lower() == "n":
		conn.close()
		break
	else:
		continue