import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 9090))

message = input('Хотите ли вы узнать время? Y/N: ')
sock.send(message.encode())
print(sock.recv(1024).decode())

while True:
	message = input('Хотите ли вы узнать время? Y/N: ')
	if message.lower() == "y":
		sock.send(message.encode())
		print(sock.recv(1024).decode())
	elif message.lower() == "n":
		sock.send(message.encode())
		break
	else:
		continue

sock.close()