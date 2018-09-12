#sudo apt-get insatll python-pip
#pip install crypto

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
import zlib
import base64
import os

def GenerateKey():
    new_key = RSA.generate(4096,e=65537)#4096 bit 512byte key length
    private_key = new_key.exportKey("PEM")#PEM format
    public_key = new_key.publickey().exportKey("PEM")

    fo = open("./RSAKey/private_key.pem","wb")
    fo.write(private_key)
    fo.close()

    fo = open("./RSAKey/public_key.pem","wb")
    fo.write(public_key)
    fo.close()

    return "\n--Success--"

def Encrypt(blob,key):
    if(key == 1):
        fo = open("./RSAKey/public_key.pem","rb")
        key = fo.read()
        fo.close()
    elif(key == 2):
        fo = open("./RSAKey/private_key.pem","rb")
        key = fo.read()
        fo.close()
    rsa_key = RSA.importKey(key)
    rsa_key = PKCS1_OAEP.new(rsa_key)

    blob = zlib.compress(blob)

    chunk_size = 470
    offset = 0
    end_loop = False
    encrypted =  b""

    while not end_loop:
        chunk = blob[offset:offset + chunk_size]
        if len(chunk) % chunk_size != 0:
            end_loop = True
            chunk += b'\x00' * (chunk_size - len(chunk))
        encrypted += rsa_key.encrypt(chunk)
        offset += chunk_size
    return base64.b64encode(encrypted)

def Decrypt(blob,key):
    if(key == 1):
         fo = open("./RSAKey/public_key.pem","rb")
         key = fo.read()
         fo.close()
    elif(key == 2):
         fo = open("./RSAKey/private_key.pem","rb")
         key = fo.read()
         fo.close()
    rsa_key = RSA.importKey(key)
    rsa_key = PKCS1_OAEP.new(rsa_key)

    blob = base64.b64decode(blob)
    
    chunk_size = 512
    offset = 0
    decrypted = b""

    while offset < len(blob):
        chunk = blob[offset: offset + chunk_size]
        decrypted += rsa_key.decrypt(chunk)
        offset += chunk_size
    return zlib.decompress(decrypted)

def sign(blob,priv_key,hashP):
    signer = PKCS1_v1_5.new(priv_key)
    if (hash == "SHA-512"):
        digest = SHA512.new()
    elif (hash == "SHA-384"):
        digest = SHA384.new()
    elif (hash == "SHA-256"):
        digest = SHA256.new()
    elif (hash == "SHA-1"):
        digest = SHA.new()
    else:
        digest = MD5.new()
    digest.update(blob)
    return signer.sign(digest)

def verify(blob,signature,pub_key,hashP):
    signer = PKCS1_v1_5.new(pub_key)
    if (hashP == "SHA-512"):
        digest = SHA512.new()
    elif (hashP == "SHA-384"):
        digest = SHA384.new()
    elif (hashP == "SHA-256"):
        digest = SHA256.new()
    elif (hashP == "SHA-1"):
        digest = SHA.new()
    else:
        digest = MD5.new()
    digest.update(blob)
    return signer.verify(digest, signature)


def DecryptionFile(key,data):
    print("The selected file is decrypting...")
    fo = open("./CryptedFile/"+data,"rb")
    value = fo.read()#.encode('ascii')
    fo.close()

    value = Decrypt(value,key)
    #buraya

    fo = open("./NonCryptedFile/"+"DE_"+data,"wb")
    fo.write(value)
    fo.close()

    return "\n--Success--"


def EncryptionFile(key,data):
    print("The selected file is encrypting...")
    fo = open("./NonCryptedFile/"+data,"rb")
    value = fo.read()
    fo.close()

    value = Encrypt(value,key)
    #buraya

    fo = open("./CryptedFile/"+"CRYPT_RSA_"+data,"wb")
    fo.write(value)
    fo.close()

    return "\n--Success--"


def selectFile(key,opinion):
        current = os.getcwd()
        if (opinion == 1):
            current += '/NonCryptedFile'
        elif(opinion == 2):
            current += '/CryptedFile'
        file_list = []
        for temp in os.listdir(current):
            file_list.append(temp)
        num = 0
        while num!=len(file_list):
            print(str(num+1)+"-) ",end="")
            print(file_list[num])
            num += 1
        value = int(input("\n\tFile Number?: "))-1
        if(opinion == 1):
            return EncryptionFile(key,file_list[value])
        elif(opinion == 2):
            return DecryptionFile(key,file_list[value])

def RSAFunc():
    print("--------------------")
    print("You can only encrypt file with public key and decrypt private key!")
    key = int(input("\n1-) Use public key\n2-) Use private key\n3-) Generate new key\n ?:"))
    if(key == 3):
        GenerateKey()
        return "\n--Success--"


    print("--------------------")
    opinion = int(input("1-) Encrypt\n2-) Decrypt\n ?:"))
    print("--------------------")
    opinion2 = int(input("\n1-) File\n ?:"))#2-) Text\n ?:"))

    print("--------------------")
    print("\n")

    if(opinion == 1):
        if(opinion2 == 1):
            return selectFile(key,opinion)
        elif(opinion2 == 2):
           # data = input("Text?:")
            data="a"
            return EncryptionText(key,data)
    elif(opinion == 2):
        if(opinion2 == 1):
            return selectFile(key,opinion)
        elif(opinion2 == 2):
            #data = input("Text?:")
            data = "a" #it will convert hex
            return DecryptionText(key,data)

