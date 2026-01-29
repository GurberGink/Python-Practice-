import os 
from time import sleep

num = int(input("Please provide a number, I will tell you whether that number is even or odd. "))
if num % 2 == 0:
    print("Even")
else:
     print("Odd")
if num % 4 == 0:
      print("This number is also a multiple of 4")

sleep(3)
os.system('clear')

num1 = int(input("Please enter a random number:  "))
num2 = int(input("Please enter a second random number: "))
os.system('clear')

print("With these two values I will calculate whether they can be divided equally or not.")
sleep(3)
os.system('clear')

if num1 % num2 == 0:
     print("This number can be divided equally :)")
else:
     print("Unfortunately these numbers cannot be divided equally")


    