import os 
from time import sleep

os.system('clear')
name = str(input("Please enter your name :) "))
print("Hello " + name + "!" + " Nice to meet you.")

sleep(2)
os.system('clear')

age = int(input("\nNow if you wouldn't mind, please enter your age :) "))
print(str(age) + ", Wow you're so young!")

sleep(2)
os.system('clear')

multiply = int(input("\nEnter a random number between 5-10 for a suprise ;)"))
currentYear = int(2026)
years = int(currentYear - age + 100)
print((str(age) + ", Wow you're so young!" + "\nYou will be 100 in the year - " + str(years) + "\n\n") * multiply)

sleep(2)
os.system('clear')

print("Terminal will terminate in t-5 seconds, Goodbye.")
sleep(5)
os.system('clear')
quit()

