import os
import sys
import ftplib

# wesite to test ftp programs: 'https://dlptest.com/ftp-test/'
host = input('Enter host: ')
user = input('Enter user: ')
password = input('Enter password: ')

try:
	ftp = ftplib.FTP(host, user=user, passwd=password)
	print('Connected to ftp server!')
except ftplib.error_perm:
	print('Error. Check whether the entered credentials are correct. Exiting program.')
	sys.exit()

def getlist():
	print('-'*22, 'NLST', '-'*22)
	files = ftp.nlst()
	for file in files:
		print(file)
	print('-'*50)

def changedir(path):
	try:
		ftp.cwd(path)
		print(f'Now in folder: {path}')
	except:
		print('Error. Unable to change path.')

def upload(path):
	if not os.path.exists(path):
		print('Process stopped, not a valid path.')
		return
	if not os.path.isfile(path):
		print('Process stopped, path not a file.')
		return
	with open(f'{path}', 'rb') as f:
		ftp.storbinary('STOR ' + path.rsplit('/', 1)[-1], f)
	print('File uploaded')

def makedir(path):
	ftp.mkd(path)
	print(f'Made direcotry {path}')

def printdir():
	ftp.pwd()

def removedir(path):
	files_raw = ftp.nlst()
	files = list(map(lambda x: (x.lower()) , files_raw))
	if path.lower() not in files:
		print('Folder not found in directory')
		return
	ftp.rmd(path)

def download(file, path):
	files_raw = ftp.nlst()
	files = list(map(lambda x: (x.lower()) , files_raw))
	if path.lower() not in files:
		print('File not found in directory')
		return
	try:
		with open(file, 'wb') as f:
			ftp.retrbinary('RETR ' + path, f.write, 2048)
		print(f'File saved as {file} in current directory.')
	except ftplib.error_perm:
		print('Error in downloading or creating the file, aborting process.')

while True:
	print('''\nEnter number to execute the function:\n1. Get list of files and folders in the directory\n2. Change directory\t\t\t3. Upload file\t\t\t4. Downolad file\n5. Make directory\t\t\t6. Remove directory\t\t7. Get current directory\nPress any other key to quit''')
	x = input('Enter key: ')
	if x == '1':
		getlist()
	elif x == '2':
		path = input('Enter folder name to navigate to: ')
		changedir(path)
	elif x == '3':
		path = input('Enter file name to upload (make sure file is in the same folder as the program): ')
		upload(path)
	elif x == '4':
		file = input('Enter file name to save content to: ')
		path = input('Enter file name from current directory of ftp server to download: ')
		download(file, path)
	elif x == '5':
		path = input('Enter folder name to create: ')
		makedir(path)
	elif x == '6':
		path = input('Enter folder name to delete: ')
		removedir(path)
	elif x == '7':
		print(f'Current directory: {ftp.pwd()}')
	else:
		ftp.quit()
		break
sys.exit()
