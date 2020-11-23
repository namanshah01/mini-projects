import requests
import threading
from queue import Queue

with open('/home/naman/Documents/python_files/subdomain_finder/subdomains-10k.txt', 'r') as f:
	subdomains = f.read().split()

def check(subdomain):
	url = f'http://{subdomain}.hackthissite.org'
	try:
		res = requests.get(url, timeout=2)
	except requests.ConnectionError:
		return
	else:
		print(f'Discovered subdomain: {url}')

queue = Queue()


for subdomain in subdomains:
	queue.put(subdomain)

def execute():
	global queue
	while not queue.empty():
		check(queue.get())

def thread(threads):
	thread_list = []

	for i in range(threads):
		thread = threading.Thread(target=execute)
		thread_list.append(thread)
	
	for thread in thread_list:
		thread.start()
	
	for thread in thread_list:
		thread.join()

thread(500)