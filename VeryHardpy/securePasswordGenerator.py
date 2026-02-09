import secrets 

upperLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowerLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specialChar = ['!','#','$','%','&','(',')','*','+','-','.','/']

while True:
        try:
            length = int(input("Choose the length of your password (length must be >= 4): "))
            if length < 4:
                print("Value must be >= 4:")
                continue
            break
        except ValueError:
            print("Enter a numerical character >= 4:")
            
    
def generate_password(length : int) -> str: 
    
    if length < 4:
        raise ValueError("Length must be four or longer.")
    
    characters = [
        secrets.choice(upperLetters),
        secrets.choice(lowerLetters),
        secrets.choice(digits),
        secrets.choice(specialChar)
    ]
    
    all_characters = upperLetters + lowerLetters + digits + specialChar
    
    for _ in range(length - 4):
        characters.append(secrets.choice(all_characters))
        
    for i in range((length)-1, 0, -1):
        j = secrets.randbelow(i + 1)
        characters[i], characters[j] = characters[j], characters[i]
        
    return print("".join(characters))


generate_password(length)
