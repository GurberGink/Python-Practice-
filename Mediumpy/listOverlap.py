import random

a = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]
b = [2, 4, 6, 8, 10, 9]
c = []

for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)

length = random.randint(1, 25)
ranlist = [random.randint(1, 100) for _ in range(length)]
ranlist2 = [random.randint(1, 100) for _ in range(length)]
overlap = []
for i in ranlist:
    if i in ranlist2:
        overlap.append(i)
print(ranlist)
print(ranlist2)
print(overlap)
