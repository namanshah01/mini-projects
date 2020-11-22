import socket
import threading

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # server.close()
# server.shutdown(socket.SHUT_RDWR)
# server.close()
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
	for client in clients:
		client.send(message)

def handle(client):
	while True:
		try:
			message = client.recv(1024)
			broadcast(message)
		except:
			index = clients.index(client)
			clients.remove(client)
			client.close()
			nickname = nicknames[index]
			broadcast(f'{nickname} left the chat.'.encode('ascii'))
			nicknames.remove(nickname)
			break

def receive():
	while True:
		client, address = server.accept()
		print(f'Connected with {address}')

		client.send('NICK'.encode('ascii'))
		nickname = client.recv(1024).decode('ascii')
		nicknames.append(nickname)
		clients.append(client)

		print(f'Nickname is {nickname}')
		broadcast(f'\r{nickname} joined!'.encode('ascii'))
		client.send('Connected to server!'.encode('ascii'))
		# client.send('Send /disconnect to leave the chat.'.encode('ascii'))

		thread = threading.Thread(target=handle, args=(client,))
		thread.start()

receive()

# issue
# when person A writes an incomplete message and person B sends the message
# A's input is erased and B's message is shown
# But the next time, A sends a message the previous part of A that was erased is still a part of the message