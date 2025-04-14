import string

input_str = input("Введіть дві літери через дефіс ")
start, end = input_str.split('-')

all_letters = string.ascii_letters
start_index = all_letters.index(start)
end_index = all_letters.index(end)

result = all_letters[start_index:end_index + 1]
print(result)
