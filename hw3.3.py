#lst1 = [1, 2, 3, 4, 5, 6] 
#lst1 = [1, 2, 3] 
#lst1 = [1, 2, 3, 4, 5] 
#lst1 = [1]
#lst1 = []

lst2 = list()

if len(lst1) % 2 != 0: #neparne
    mid = (len(lst1) + 1) // 2
    lst2.append(lst1[:mid])
    lst2.append(lst1[mid:])
elif len(lst1) % 2 == 0: 
    mid = len(lst1) // 2
    lst2.append(lst1[:mid])
    lst2.append(lst1[mid:])

print(lst2)