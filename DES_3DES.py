from pyDes import *
import base64
import zlib
import os

def EncryptionText(key,data,section):
    if(section=="3DES"):
        k =triple_des(key, CBC,"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    else:
        k =des(key, CBC,"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    d = k.encrypt(data)
   
    print(d)
    for temp in str(d):
        print("%0.2x " %ord(temp),end="")
   
    fo = open("EncryptFile","wb")
    encoded = base64.b64encode(d)
    fo.write(encoded)
    fo.close()

    return "\nSuccess"

def DecryptionText(key,data,section):
    if(section=="3DES"):
        k =triple_des(key, CBC,"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    else:
        k =des(key, CBC,"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    
    fo = open("EncryptFile","r")
    encoded = fo.read()
    fo.close()
    decoded = base64.b64decode(encoded)
    d = (k.decrypt(decoded)).decode('ascii')

    print(d)
    return "\nSuccess"

def EncryptionFile(key,data,section):
    if(section=="3DES"):
        name= "3DES"
        k =triple_des(key, CBC,"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    else:
        name = "DES"
        k =des(key, CBC,"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
       
    print("The selected file is encrypting...")
    fo = open("./NonCryptedFile/"+data,"rb")
    indexData = fo.read()
    fo.close()
       
    indexData = zlib.compress(indexData)
    d = k.encrypt(indexData)

    fo = open("./CryptedFile/"+"CRYPT_"+name+"_"+data,"wb")
    encoded = base64.b64encode(d)
    fo.write(encoded)
    fo.close()
    
    return "\n--Success--"

def DecryptionFile(key,data,section):
    if(section=="3DES"):
        name= "3DES"
        k =triple_des(key, CBC,"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    else:
        name = "DES"
        k =des(key, CBC,"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

    print("The selected file is decrypting...")
    fo = open("./CryptedFile/"+data,"rb")
    indexData = fo.read()
    fo.close()
    decoded = base64.b64decode(indexData) #.decode('ascii')
    d = (k.decrypt(decoded))
    d = zlib.decompress(d)

        
    fo = open("./NonCryptedFile/"+"DE_"+data,"wb")
    #print(d)
    fo.write(d)
    fo.close()

    return "\n--Success--"

def selectFile(key,opinion,section):
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
        return EncryptionFile(key,file_list[value],section)
    elif(opinion == 2):
        return DecryptionFile(key,file_list[value],section)



def DES():
    section = "DES"
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
            return selectFile(key,opinion,section)
        elif(opinion2 == 2):
            data = input("Text?:")
            return EncryptionText(key,data,section)
    elif(opinion == 2):
        if(opinion2 == 1):
            return selectFile(key,opinion,section)
        elif(opinion2 == 2):
            #data = input("Text?:")
            data = "a" #it will convert hex
            return DecryptionText(key,data,section)

def Triple_DES():
    section = "3DES"
    print("--------------------")
    opinion = int(input("1-) Encrypt\n2-) Decrypt\n ?:"))
    print("--------------------")
    opinion2 = int(input("\n1-) File\n2-) Text\n ?:"))
    
    print("--------------------")
    key = input("\nEnter 16byte or 24byte key: ")
    print("\n")

    if (not(len(key)== 16 or len(key)==24)):
            print("Key Error!")
            return "Error"
    

    if(opinion == 1):
        if(opinion2 == 1):
            return selectFile(key,opinion,section)
        elif(opinion2 == 2):
            data = input("Text?:")
            return EncryptionText(key,data,section)
    elif(opinion == 2):
        if(opinion2 == 1):
            return selectFile(key,opinion,section)
        elif(opinion2 == 2):
            #data = input("Text?:")
            data = "a" #it will convert hex
            return DecryptionText(key,data,section)


