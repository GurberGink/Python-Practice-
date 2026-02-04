status = True 

while status:
    a = int(input("Enter a value: "))
    b = int(input("Enter another value: "))

    container = list(range(a,b))
    
    choice = input("would you like the sum or average of the list? Please type a for average and s for sum: ")
    
    if choice == "a":
        print((a + b)/2)
        
    elif choice == "s":
        print(sum(container))
    
    check = input("would you like to play again? Y for yes | N for no. ").capitalize()
    
    if check == "N":
        break
    
    elif check == "Y":
        print("Okay let's play again. ")
    
    else:
        print("Okay let's play again. ")
    