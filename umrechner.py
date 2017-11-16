#Autor = Jonah Zürcher
#Date = 21/10/2017
#Switzerland CH
#Writte in Python3.5 IDLE
import time
zahl = str(0)
option = ""

def printMenu():

    for i in range(6):
        print("\n")

    print("""         ***********************************************
         **               Umrechner                   **
         ***********************************************
         **             Option wählen                 **
         ***********************************************
         **  (0) Zahl eingeben                        **
         **  (1) Dezimal zu Binär                     **
         **  (2) Dezimal zu Hexadezimal               **
         **  (3) Binär zu Dezimal                     **
         **  (4) Binär zu Hexadezimal                 **
         **  (5) Hexadezimal zu Dezimal               **
         **  (6) Hexadezimal zu binär                 **
         **  (p) Zeige Menu                           **
         **  (x) Beenden                              **
         ***********************************************""")
    print("     ******************************************************")
    print("      Input: " + zahl) 
    print("     ******************************************************")

printMenu()
zahl = input("Geben sie eine Zahl ein: ")
printMenu()

while option.lower() != "x":

    try:
        option = input("Wählen sie ein Option: ")

        if option == "0":
            zahl = input("Geben sie eine Zahl ein: ")
            printMenu()
            
        elif option == "1":
            def binary(number):
                return int("".join(bin(number).split('0b')))
            ausgabe = binary(int(zahl))
            print("Die Zahl " + zahl + " ist umgewandelt:  " + str(ausgabe))
            
        elif option == "2":
            def hexa(number):
                return "".join(hex(number).split("0x"))
            ausgabe = hexa(int(zahl))
            print("Die Zahl " + zahl + " ist umgewandelt:  " + str(ausgabe).upper())
            
        elif option == "3":
            def dezimal(number):
                zahl1 = ("0b"+str(number))
                return int(zahl1,2)
            ausgabe = dezimal(int(zahl))
            print("Die Zahl " + zahl + " ist umgewandelt:  " + str(ausgabe))
        
        elif option == "4":
            def hexa(number):
                zahl1 = ("0b"+str(number))
                zahl2 = int(zahl1,2)
                return "".join(hex(zahl2).split('0x'))
            ausgabe = hexa(int(zahl))
            print("Die Zahl " + zahl + " ist umgewandelt:  " + str(ausgabe).upper())

        elif option == "5":
            def dezimal(number):
                zahl1 = ("0x"+str(number))
                return "".join(zahl1.split("0x"))
            ausgabe = dezimal(int(zahl.lower(),16))
            print("Die Zahl " + zahl + " ist umgewandelt:  " + str(ausgabe))

        elif option == "6":
            def binary(number):
                zahl1 = ("0x"+str(number))
                return int("".join(bin(number).split('0b')))
            ausgabe = binary(int(zahl.lower(),16))
            
            print("Die Zahl " + zahl + " ist umgewandelt:  " + str(ausgabe))
        elif option.lower() == "p":
            printMenu()

        elif option.lower() == "x":
            break
        
        else:
            print("Ihre Eingabe ist ungültig!")
            time.sleep(2)
            printMenu()
            
    except ValueError:
        for i in range(6):
            print("\n")
        print("""
Die eingegeben Zahl ist nicht mit der gewünschten Option kombinierbar!

Bitte geben sie entweder eine neue Zahl (Option 0) ein, oder wählen sie eine andere Option!
Sie werden zum Menu weitergeleitet""")
        time.sleep(7)
        printMenu()
    
