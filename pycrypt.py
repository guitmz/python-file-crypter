import random, base64
from hashlib import sha1

def crypt(data, key): #RC4 Alg
    x = 0
    box = range(256)
    for i in range(256):
        x = (x + box[i] + ord(key[i % len(key)])) % 256
        box[i], box[x] = box[x], box[i]
    x = y = 0
    out = []
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))

    return ''.join(out)

def encrypt(data, key, encode=base64.b64encode, salt_length=16): #RC4 with random salt and base64 encoding"
    salt = ''
    for n in range(salt_length):
        salt += chr(random.randrange(256))
    data = salt + crypt(data, sha1(key + salt).digest())
    if encode:
        data = encode(data)
    return data

def decrypt(data, key, decode=base64.b64decode, salt_length=16):
    if decode:
        data = decode(data)
    salt = data[:salt_length]
    return crypt(data[salt_length:], sha1(key + salt).digest())

def choose():
	destiny = raw_input("Enter 'E' to encrypt a file or 'D' to decrypt: ")
	return destiny


destiny = choose()


if destiny == 'E':
	fiilepath = raw_input("Enter the path of the file you want to encrypt: ")
	originalf = open(fiilepath, "rb")
	file = originalf.read()
	originalf.close()
	destpath = raw_input("Enter the destination path of the encrypted file (file can have any extension): ")
	key =  raw_input("Enter a key to encrypt the file: ")
	data = encrypt(file, key)
	dest = open(destpath, "wb")
	dest.write(data)
	dest.close()
	exit()
	

elif destiny == 'D':
	fiilepath = raw_input("Enter the path of the file you want to decrypt: ")
	originalf = open(fiilepath, "rb")
	file = originalf.read()
	originalf.close()
	destpath = raw_input("Enter the destination path of the encrypted file (file can have any extension): ")
	key =  raw_input("Enter the key to decrypt the file: ")
	dest = open(destpath, "wb")
	data = decrypt(file, key)
	dest = open(destpath, "wb")
	dest.write(data)
	dest.close()
	exit()

elif destiny != 'D' and destiny != 'E':
	print "Wrong input!"




