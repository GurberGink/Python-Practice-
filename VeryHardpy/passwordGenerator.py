import secrets

upperLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowerLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specialChar = ['!','#','$','%','&','(',')','*','+','-','.','/']

def main():
    password = []
    
    length = int(input("Please enter the length you'd like your password to be: "))
        
    for i in range(length):
        category = secrets.choice([1, 2, 3, 4])
        
        if category == 1:
            password.append(secrets.choice(upperLetters))
        elif category == 2:
            password.append(secrets.choice(lowerLetters))
        elif category == 3:
            password.append(secrets.choice(digits))
        elif category == 4:
            password.append(secrets.choice(specialChar))

    password = "".join(password)
    return password
     
print(main())