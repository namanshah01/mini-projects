import sys
import os
import random

# switching to current running python files directory
os.chdir('\\'.join(__file__.split('/')[:-1]))

# handling possible errors
fname = input('Enter name of text file: ')
if fname.split('.')[-1] != 'txt':
    print('Please enter the name of a text file')
    sys.exit()
if not os.path.isfile(fname):
    print('File does not exist')
    sys.exit()

fh = open(fname, 'r')
lines = fh.readlines()
fh.close()

enc_key = random.randint(1, 1000)

final = []
for line in lines:
    line = line.strip()
    new = []
    for letter in line:
        new.append(str(ord(letter)*enc_key))
    final.append('@#'.join(new))

print(f'The key to decrypt encoded file is: {enc_key}')
desc = input('Do you wish to save the key(y/n)')
if desc == 'y':
    fh = open('key_' + fname, 'w')
    fh.write(str(enc_key))
    print('Key saved in current directory')

# fname = 'encoded_' + fname
fh = open(fname, 'w')
fh.write('&%&%'.join(final))
fh.close()