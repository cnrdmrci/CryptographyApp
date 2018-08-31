from DES import DES
import os

while True:
    #os.system('clear')
    print("--------------------------------------------------")
    print ("""\n Welcome to CryptographyApp, Written by Caner..
            
            Select:
                1-) DES
                2-) 3DES
                3-) AES
                4-) RSA
                5-) MD5
                6-) SHA256
                7-) Exit

         Your opinion? : """,end = "")
    opinion = int(input())
    if(opinion == 7) : break

    elif(opinion == 1):
        print("--------------------")
        print ("Your have selected DES\n")
        print (DES())

    elif(opinion == 2):
        print("--------------------")
        print ("Your have selected 3DES")
        #print(3DES())

    elif(opinion == 3):
        print ("Your have selected AES")

    elif(opinion == 4):
        print ("Your have selected RSA")

    elif(opinion == 5):
        print ("Your have selected MD5")

    elif(opinion == 6):
        print ("Your have selected SHA256")
    else:
        print("Wrong selection")

