import hashlib

def md5lock(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()

def sha256lock(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def sha512lock(string):
    hash_object = hashlib.sha512(string.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

def md5():
    key = input("Enter key: ")
    return md5lock(key)

def sha256():
    key = input("Enter key: ")
    return sha256lock(key)

def sha512():
    key = input("Enter key: ")
    return sha512lock(key)

