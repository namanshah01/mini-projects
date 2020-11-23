import requests
import threading
from queue import Queue

domain = 'hackthissite.org'

with open('subdomains-10k.txt', 'r') as f:
	subdomains = f.read().split()[:1000]

def check(subdomain):
	global domain
	url = f'http://{subdomain}.{domain}'
	try:
		res = requests.get(url, timeout=2)
	except requests.ConnectionError:
		return
	else:
		print(f'Discovered subdomain: {url}')

for subdomain in subdomains:
	check(subdomain)
