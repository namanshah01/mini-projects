import sys
import os
import random

# switching to current running python files directory
os.chdir('\\'.join(__file__.split('/')[:-1]))

fname = input('Enter name of text file: ')

# handling possible errors
fname = input('Enter name of text file: ')
if fname.split('.')[-1] != 'txt':
    print('Please enter the name of a text file')
    sys.exit()
if not os.path.isfile(fname):
    print('File does not exist')
    sys.exit()

fh = open(fname, 'r')
lines = fh.read()
fh.close()

if os.path.isfile('key_' + fname):
	fh = open('key_' + fname, 'r')
	key = int(fh.read().strip())
	fh.close()
	os.remove('key_' + fname)
else:
	key = int(input('Enter key: '))

fin = []
lines = lines.split('&%&%')
for line in lines:
    new = []
    letter = line.split('@#')
    for l in letter:
        if l == '':
            continue
        new.append(chr(int(l)//key))
    fin.append(''.join(new))

fh = open(fname, 'w')
fh.write('\n'.join(fin))
fh.close()