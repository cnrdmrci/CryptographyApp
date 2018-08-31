from pyDes import *
import base64
import zlib
import os

def EncryptionText(key,data):
    k =des(key, CBC,"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    d = k.encrypt(data)
   
    print(d)
    for temp in str(d):
        print("%0.2x " %ord(temp),end="")
   
    fo = open("EncryptFile","wb")
    encoded = base64.b64encode(d)
    fo.write(encoded)
    fo.close()

    return "\nsuccess"

def DecryptionText(key,data):
    k = des(key, CBC,"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    
    fo = open("EncryptFile","r")
    encoded = fo.read()
    fo.close()
    decoded = base64.b64decode(encoded)
    d = (k.decrypt(decoded)).decode('ascii')

    print(d)
    return "\nsuccess"

def EncryptionFile(key,data):
        k =des(key, CBC,"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
       
        print("The selected file is encrypting...")
        fo = open("./NonCryptedFile/"+data,"rb")
        indexData = fo.read()
        fo.close()
        
        indexData = zlib.compress(indexData)
        d = k.encrypt(indexData)

        fo = open("./CryptedFile/"+"CRYPT"+data,"wb")
        encoded = base64.b64encode(d)
        fo.write(encoded)
        fo.close()
        
        return "\n--Success--"

def DecryptionFile(key,data):
        k =des(key, CBC,"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

        print("The selected file is decrypting...")
        fo = open("./CryptedFile/"+data,"rb")
        indexData = fo.read()
        fo.close()
        decoded = base64.b64decode(indexData) #.decode('ascii')
        d = (k.decrypt(decoded))
        d = zlib.decompress(d)

        
        fo = open("./NonCryptedFile/"+"DE"+data,"wb")
        #print(d)
        fo.write(d)
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



def DES():
    print("--------------------")
    opinion = int(input("1-) Encrypt\n2-) Decrypt\n ?:"))
    print("--------------------")
    opinion2 = int(input("\n1-) File\n2-) Text\n ?:"))
    
    print("--------------------")
    key = input("\nEnter 8byte key: ")
    print("\n")

    if (len(key) != 8):
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

