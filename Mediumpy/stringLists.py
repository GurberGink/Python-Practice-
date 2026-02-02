import os
from time import sleep

os.system("clear")

while True:
    string = str(input("\nPlease enter a palindrome "))
    p = string[::-1]

    if string == p:
        os.system("clear")
        sleep(1)
        print("True, this is in fact a palindrome")
        break
    else:
        os.system("clear")
        sleep(1)
        print("False, this is in fact not a palindrome. Please try again :)")
