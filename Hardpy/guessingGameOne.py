import random 
import os
from time import sleep
 
yesOrNo = ["Yes", "No"]
status = True 
answer = random.randint(1,9)
tally = 0

os.system("clear")

while status:
    while True:
        try:
            guess = int(input("Please enter a value 1 - 9 \n\t"))
            
            if guess >= 1 and guess <= 9:
                break
            
            else:
                os.system("clear")
                
        except ValueError:
            os.system("clear")
            print("Please enter a valid integer. ") 
            sleep(1)
            os.system("clear")            
            
    if guess == answer:
        print("\nCongratulations that was correct")
        tally += 1
        
        
    elif guess < answer:
        print("\nThe guess is too low")
        sleep(1)
        os.system("clear")
        tally += 1
        
    elif guess > answer:
        print("\nThe guess was too high")
        sleep(1)
        os.system("clear")
        tally += 1
    
    if guess == answer:
        sleep(1)
        os.system("clear")
        print("It took you", tally, "attempts to guess the number!\n\n")
        sleep(2)
        os.system("clear")
        check = input("Would you like to play again? \n\t Yes|No\n\n\t  ").capitalize()
    
        while check not in yesOrNo:
            print("This input is invalid. Please try again.")
            check = input("Would you like to play again? \n\t Yes|No\n\n\t  ").capitalize()
            
        if check == "No":
            os.system("clear")
            print("Thank you for playing :)")
            sleep(3)
            status = False
            
        elif check == "Yes":
            os.system("clear")
            print("Okay lets play again :)")
            sleep(3)
            os.system("clear")
            answer = random.randint(1,9)
        

