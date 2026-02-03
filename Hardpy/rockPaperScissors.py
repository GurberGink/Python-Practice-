import os
from time import sleep

decisions = ["Rock", "Paper", "Scissors"]
yesOrNo = ["Yes", "No"]
status = True

os.system("clear")
sleep(0.5)

print(
    "I see you'd like to play Rock, Paper, Scissors. \nThis a two player game requiring a single decision from each player each round. "
)

sleep(5)
os.system("clear")

while status:
    player1 = str(
        input("Player One, please choose: Rock|Paper|Scissors \n\n")
    ).capitalize()
    sleep(0.5)

    while player1 not in decisions:
        os.system("clear")
        print("This input is invalid. Please try again.\n")
        player1 = str(
            input("Player One, please choose: Rock|Paper|Scissors \n\n")
        ).capitalize()
    sleep(0.5)
    os.system("clear")

    player2 = str(
        input("Player Two, please choose: Rock|Paper|Scissors \n\n")
    ).capitalize()
    sleep(0.5)

    while player2 not in decisions:
        os.system("clear")
        print("This input is invalid. Please try again.\n")
        player2 = str(
            input("Player Two, please choose: Rock|Paper|Scissors \n\n")
        ).capitalize()
    sleep(0.5)
    os.system("clear")

    print("Calculating.")
    sleep(0.7)
    print("Calculating..")
    sleep(0.7)
    print("Calculating...")
    sleep(0.7)
    print("Calculating....")
    sleep(0.7)
    print("\nResults finalised :) ")
    sleep(1.7)

    os.system("clear")

    if player1 == player2:
        print("The game is a tie both Player One and Two selected: " + player1 + "!\n")

    elif player1 == decisions[0] and player2 == decisions[1]:
        print(
            "Player Two wins by choice of "
            + player2
            + " where Player One chose "
            + player1
            + "!\n"
        )

    elif player1 == decisions[0] and player2 == decisions[2]:
        print(
            "Player One wins by choice of "
            + player1
            + " where Player Two chose "
            + player2
            + "!\n"
        )

    elif player1 == decisions[1] and player2 == decisions[0]:
        print(
            "Player One wins by choice of "
            + player1
            + " where Player Two chose "
            + player2
            + "!\n"
        )

    elif player1 == decisions[1] and player2 == decisions[2]:
        print(
            "Player Two wins by choice of "
            + player2
            + " where Player One chose "
            + player1
            + "!\n"
        )

    elif player1 == decisions[2] and player2 == decisions[0]:
        print(
            "Player Two wins by choice of "
            + player2
            + " where Player One chose "
            + player1
            + "!\n"
        )

    elif player1 == decisions[2] and player2 == decisions[1]:
        print(
            "Player One wins by choice of "
            + player1
            + " where Player Two chose "
            + player2
            + "!\n"
        )

    sleep(4)
    os.system("clear")

    check = str(input("Would you like to play again? \n\t Yes|No\n\n\t  ")).capitalize()

    while check not in yesOrNo:
        print("This input is invalid. Please try again.")
        sleep(1)
        os.system("clear")
        check = str(
            input("Would you like to play again? \n\t Yes|No\n\n\t  ")
        ).capitalize()

    if check == "No":
        os.system("clear")
        print("Thank you for playing :)")
        sleep(3)
        break

    elif check == "Yes":
        os.system("clear")
        print("Okay lets play again :)")
        sleep(3)
        os.system("clear")
