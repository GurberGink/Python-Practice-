list1 = [1, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 7, 8, 9, 10, 10]

def removeDuplicates(l):
    noDupes = []
    
    for i in l:
        if i not in noDupes:
            noDupes.append(i)
    
    print(noDupes)
    return noDupes
    
removeDuplicates(list1)

def removeDupes(l):
    
    l = list(set(l))
    print(l)
    return l    

removeDupes(list1)
