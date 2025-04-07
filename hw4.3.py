import random

length = random.randint(3, 10)

original = [random.randint(0, 100) for i in range(length)]

new_list = [original[0], original[2], original[-2]]

print(original)
print(new_list)