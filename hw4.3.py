import random

length = random.randint(3, 10)
original = []

for i in range(length):
    num = random.randint(0, 100)  
    original.append(num)      

new_list = [original[0], original[2], original[-2]]

print(original)
print(new_list)
