import random

list1 = random.sample(range(100), random.randint(5, 20))
list2 = random.sample(range(100), random.randint(5, 20))

commonInList = [x for x in list1 if x in list2]
print(list1)
print(list2)
print(commonInList)
