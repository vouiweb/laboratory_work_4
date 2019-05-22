import socket

print("The server has started successfull..\nPort: 9090")

def func(data):
	a, b, c = data[0], data[1], data[2]
	if c != a:
	    return abs(1 - a*b**c - a*(b**2 - c**2) + (b - c + a) * (12 + b)/(c-a))
	else:
		return "Деление на 0 невозможно!"

sock = socket.socket()
sock.bind(('', 9090))
sock.listen()
conn, addr = sock.accept()

print('\nСonnected:', addr)

while True:
	data = conn.recv(1024).decode().strip().split(' ')
	data = [int(x) for x in data]
	if data == "n":
		conn.close()
		break
	else:
		answer = str(func(data))
		conn.send(answer.encode())