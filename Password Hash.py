import hashlib #The hashing library
import getpass #To make the typing invisible
import pyperclip #To Copy the string

string = getpass.getpass('> ')
hash = hashlib.sha256(string.encode()).hexdigest()
hash = hashlib.sha512(hash.encode()).hexdigest()
pyperclip.copy(hash)
print('Done.')