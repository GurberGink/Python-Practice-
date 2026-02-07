text = input("Please enter a sentence containing multiple strings here: ")

def reverseString(a):
    result = a.split()
    return " ".join(reversed((result)))
    
print(reverseString(text))

# a.split splits string into secitons in a list, .join(reversed) returns the list in a reversed order of strings 
