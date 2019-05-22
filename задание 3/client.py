import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 9090))

matrix = ''
for i in range(0,3):
	matrix += input(f'Заполните {i+1}-ый ряд матрицы: ') + ' '

sock.send(matrix.encode())
print(sock.recv(1024).decode())

while True:
	for i in range(0,3):
		matrix += input(f'Заполните {i+1}-ый ряд матрицы: ') + ' '
	sock.send(matrix.encode())
	print(sock.recv(1024).decode())