def getInteger(helpText = "Please enter a value: "):
    return int(input(helpText))

status = True
def getPrimeNumber():
    primeNumber = getInteger()
    b = []
    i = 1

    while i <= primeNumber:
        if primeNumber % i == 0:
            b.append(i)
        i += 1
        
    
    if len(b) == 2:
        print(str(primeNumber) + " This is a prime number. ")
        
    else:
        print("This is not a prime number as " + str(primeNumber) + " is divisible by: " + str(b))
        status = False
    
getPrimeNumber()

            
        
        
    



