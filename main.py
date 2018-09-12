from DES_3DES import DES,Triple_DES
from AESCode import AESFunc
from RSACode import RSAFunc
from MD5 import *
import os 

while True:
    #os.system('clear')
    print("--------------------------------------------------")
    print ("""\n Welcome to CryptographyApp, Written by Caner..
            
            Select:
                1-) DES Encryption
                2-) 3DES Encryption
                3-) AES Encryption
                4-) RSA Encryption
                5-) MD5 Encryption
                6-) SHA256 Encryption
                7-) SHA512 Encryption
                0-) Exit

         Your opinion? : """,end = "")
    opinion = int(input())
    if(opinion == 0) : break

    elif(opinion == 1):
        print("--------------------")
        print ("Your have selected DES\n")
        print (DES())

    elif(opinion == 2):
        print("--------------------")
        print ("Your have selected 3DES")
        print(Triple_DES())

    elif(opinion == 3):
        print("--------------------")
        print ("Your have selected AES")
        print(AESFunc())

    elif(opinion == 4):
        print("--------------------")
        print ("Your have selected RSA")
        print(RSAFunc())

    elif(opinion == 5):
        print("--------------------")
        print ("Your have selected MD5")
        print(md5())

    elif(opinion == 6):
        print("--------------------")
        print ("Your have selected SHA256")
        print(sha256())

    elif(opinion == 7):
        print("--------------------")
        print ("Your have selected SHA512")
        print(sha512())

    else:
        print("--------------------")
        print("Wrong selection")

