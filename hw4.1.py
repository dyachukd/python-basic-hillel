# lst1 = [0, 1, 0, 12, 3] 
# lst1 = [0]
#lst1 = [1, 0, 13, 0, 0, 0, 5]
# lst1 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] 
lst1 = [0, 1, 0, 12, 3] 

i = 0
position = 0
n = len(lst1)

while i < n:
    if lst1[position] == 0:
            a = lst1.pop(position)
            lst1.append(a)
            i = i + 1
    else:
            position = position + 1
            i = i + 1
            
print(lst1)
