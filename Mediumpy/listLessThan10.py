a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
a.append(11)
test = int(input("Enter a value 1-10: "))
for num in a:
    if num < test:
        b.append(num)
        b.sort()
print(b)
print()
