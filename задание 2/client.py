import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 9090))

print("\nЧтобы закрыть программу, введите N: ")
message = input('Введите значения[a, b, c] через пробел: Y/N: ')
sock.send(message.encode())
print(sock.recv(1024).decode())

while True:
	message = input('\nВведите значения через пробел: ')
	if message == "n":
		sock.send(message.encode())
		break
	else:
		sock.send(message.encode())
		print(sock.recv(1024).decode())

sock.close()