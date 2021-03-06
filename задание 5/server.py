import socket

print("The server has started successfull..\nPort: 9090")

def det(data):
	return data[0] * data[3] - data[1] * data[2]

sock = socket.socket()
sock.bind(('', 9090))
sock.listen()
conn, addr = sock.accept()

print('\nСonnected:', addr)

while True:
	data = conn.recv(1024).decode().strip().split(' ')
	data = [int(x) for x in data]
	answer = str(det(data))
	conn.send(answer.encode())