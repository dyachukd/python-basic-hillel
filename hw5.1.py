var_name = input("Введіть ім'я змінної: ")

keywords = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
    'except', 'finally', 'for', 'from', 'global', 'if', 'import',
    'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
    'return', 'try', 'while', 'with', 'yield'
]

is_valid = True

if var_name == "_":
    is_valid = True

elif var_name.count("_") > 1:
    is_valid = False

elif var_name == "" or var_name[0] in '0123456789':
    is_valid = False

elif var_name in keywords:
    is_valid = False

else:
    for char in var_name:
        if 'A' <= char <= 'Z':
            is_valid = False
            break
        if not ('a' <= char <= 'z' or '0' <= char <= '9' or char == '_'):
            is_valid = False
            break

print(is_valid)