number = int(input("Please enter a prime number. "))
a = [x for x in range(2, number) if number % x == 0]

def primeNumbers(v):
    if number > 1:
        if len(a) == 0:
            print("This is a prime number.")
        else:
            print("This is not a prime number.")
    else:
        ("This is a prime number.")
    
primeNumbers(number)
        
