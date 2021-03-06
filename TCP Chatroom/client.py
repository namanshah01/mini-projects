import sys
import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.close()
# client.shutdown(socket.SHUT_RDWR)
# client.close()
client.connect(('127.0.0.1', 55555))

nickname = input('Choose a nickname: ')

def receive():
	while True:
		try:
			message = client.recv(1024).decode('ascii')
			if message == 'NICK':
				client.send(nickname.encode('ascii'))
			elif message[:message.find(':')] != nickname:
				print(message)
			# elif message.split()[-1] == '/disconnect':
			# 	sys.exit()
			# 	# print('Disconnected from the server. Terminating program.1')
			# 	client.close()
			# 	# print('Disconnected from the server. Terminating program.2')
			# 	client.shutdown(socket.SHUT_RDWR)
			# 	# print('Disconnected from the server. Terminating program.3')
			# 	sys.exit()
		except:
			print('An error occured. Disconnecting from the server.')
			client.close()
			sys.exit()
			break

def write():
	while True:
		message = f'{nickname}: {input()}'
		client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
