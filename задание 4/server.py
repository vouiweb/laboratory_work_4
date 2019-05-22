import socket

print("The server has started successfull..\nPort: 9090")

sock = socket.socket()
sock.bind(('', 9090))
sock.listen()
conn, addr = sock.accept()
last_message = 'У вас нет сообщений...'

while True:
	message = conn.recv(1024).decode()
	if message.lower() == "n":
		sock.close()
		break
	conn.send(last_message.encode())
	last_message = message