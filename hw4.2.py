lst = [0, 1, 7, 2, 4, 8] 
#lst = [1, 3, 5] 
#lst = [6] 
#lst = [] 

if not lst:
        print(0) 
else:    
    sum = 0
    i = 0
    while i < len(lst):
            if i % 2 == 0:
                sum += lst[i]
            i += 1
    print( sum * lst[-1])