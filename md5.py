import hashlib

hashstring = input("Enter a string to md5 hash: ")

print(hashlib.md5(hashstring.encode('utf-8')).hexdigest())