a = range(1, 100)
b = [] 
num = int(input("Enter a number to see it's divisors: "))

for i in a:
    if num % i == 0:
        b.append(i)
print(b)