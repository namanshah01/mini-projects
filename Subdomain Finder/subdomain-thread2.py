import requests
import threading
from queue import Queue

def create_queue():
	global queue
	with open('/home/naman/Documents/python_files/subdomain_finder/subdomains-10k.txt', 'r') as f:
		subdomains = f.read().split()[:1000]
	for subdomain in subdomains:
		queue.put(subdomain)

def check(subdomain):
	global domain
	url = f'http://{subdomain}.hackthissite.org'
	# url = f'http://{subdomain}.{domain}'
	try:
		res = requests.get(url, timeout=2)
	except requests.ConnectionError:
		return
	else:
		print(f'Discovered subdomain: {url}')

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

queue = Queue()
create_queue()
# domain = 'hackthissite.org'
thread(500)
