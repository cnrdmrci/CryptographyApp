import base64
from Crypto.Cipher import AES
from Crypto import Random
import zlib
import os
import sys

default = "12345678123456781234567812345678"

class AESCipher:
        BS = 16
        def __init__(self,key):
                self.key = key
        def encrypt(self,raw):
                raw = self.pad(raw)
                iv = Random.new().read(AES.block_size)
                cipher = AES.new(self.key,AES.MODE_CBC,iv)
                return base64.b64encode(iv+cipher.encrypt(raw))
        def decrypt(self,enc):
                enc= base64.b64decode(enc)
                iv = enc[:16]
                cipher = AES.new(self.key,AES.MODE_CBC,iv)
                return self.unpad(cipher.decrypt(enc[16:]))
        def pad(self,s):
                return s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)
        def unpad(self,s):
                return s[:-ord(s[len(s)-1:])]

def EncryptionText(key,data):
    temp_obj = AESCipher(key)
    value = temp_obj.encrypt(data)

    print("Encrypted data: " + str(value.decode('ascii')))

    fo = open("EncryptFileAes","wb")
    fo.write(value)
    fo.close()
    
    return "\nSuccess"

def DecryptionText(key,data):
    fo = open("EncryptFileAes","rb")
    value = fo.read()
    fo.close()

    temp_obj = AESCipher(key)
    value = temp_obj.decrypt(value)

    print(value.decode('ascii'))

    return "\nSuccess"

def EncryptionFile(key,data):
    print("The selected file is encrypting...")
    fo = open("./NonCryptedFile/"+data,"rb")
    indexData = fo.read()
    fo.close()

    indexData = zlib.compress(indexData)
    indexData = base64.b64encode(indexData).decode('ascii')
    temp_obj = AESCipher(key)
    value = temp_obj.encrypt(indexData)

    fo = open("./CryptedFile/"+"CRYPT_AES_"+data,"wb")
    fo.write(value)
    fo.close()

    return "\n--Success--"
   
def DecryptionFile(key,data):
    print("The selected file is decrypting...")
    fo = open("./CryptedFile/"+data,"rb")
    value = fo.read()#.encode('ascii')
    fo.close()

    temp_obj = AESCipher(key)
    value = temp_obj.decrypt(value)
    value = base64.b64decode(value)
    value = zlib.decompress(value)

    fo = open("./NonCryptedFile/"+"DE_"+data,"wb")
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


def AESFunc():
    print("--------------------")
    opinion = int(input("1-) Encrypt\n2-) Decrypt\n ?:"))
    print("--------------------")
    opinion2 = int(input("\n1-) File\n2-) Text\n ?:"))

    print("--------------------")
    key = default
    #key = input("\nEnter 16byte(128bit) or 24byte(192bit) or 32byte(256) \nkey: ")
    print("\n")

    if(not(len(key)==16 or len(key)==24 or len(key)==32)):
        print("Key Error!")
        return "Error"

    if(opinion == 1):
        if(opinion2 == 1):
            return selectFile(key,opinion)
        elif(opinion2 == 2):
            data = input("Text?:")
            return EncryptionText(key,data)
    elif(opinion == 2):
        if(opinion2 == 1):
            return selectFile(key,opinion)
        elif(opinion2 == 2):
            #data = input("Text?:")
            data = "a" #it will convert hex
            return DecryptionText(key,data)



