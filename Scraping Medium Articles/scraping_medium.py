import os
import sys
import requests
import re
from bs4 import BeautifulSoup

# switching to current running python files directory
# os.chdir('\\'.join(__file__.split('/')[:-1]))

def get_page(url):
	if (url[:18] != 'https://medium.com') and (url[:17] != 'http://medium.com'):
		print('Please enter a valid website, or make sure it is a medium article')
		sys.exit(1)
	res = requests.get(url)
	res.raise_for_status()
	soup = BeautifulSoup(res.text, 'html.parser')
	return soup

def purify(text):
    rep = {"<br>": "\n", "<br/>": "\n", "<li>":  "\n"}
    rep = dict((re.escape(k), v) for k, v in rep.items()) 
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    text = re.sub('\<(.*?)\>', '', text)
    return text

def collect_text(soup):
	fin = ''
	main = (soup.head.title.text).split('|')
	fin += f'Title:   {main[0].upper()}\n{main[1]}'

	header = soup.find_all('h1')
	j = 1

	fin += f'\n\n{header[j].text.upper()}'
	for elem in header[j].next_siblings:
		if elem.name == 'h1':
			j+=1
			fin += f'\n\n{header[j].text.upper()}'
			continue
		fin += f'\n{purify(str(elem))}'
	return fin

def save_file(fin):
	with open('scraped_article.txt', 'w', encoding='utf8') as outfile:
		outfile.write(fin)

# https://medium.com/coding-blocks/one-stop-guide-to-google-summer-of-code-a9e803beeda7
url = input('Enter url of a medium article: ')
soup = get_page(url)
fin = collect_text(soup)
save_file(fin)