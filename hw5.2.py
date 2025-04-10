new_operation = True

while new_operation == True: 
    first_num = int(input("введіть перше число: "))
    operator = input("введіть оператор: ")
    second_num = int(input("введіть друге число: "))

    if operator == "+":
        result = first_num + second_num
        print("Результат:", result)
    elif operator == "-":
        result = first_num - second_num
        print("Результат:", result)
    elif operator == "*":
        result = first_num * second_num
        print("Результат:", result)
    elif operator == "/":
        if second_num == 0:
            print("Помилка, ділення на нуль неможливе.")
        else:
            result = first_num / second_num
            print("Результат:", result)
    else:
        print("Невідома операція, введіть коректний оператор")

    new_operation = input("Продовжити роботу?")
    if new_operation.lower() in ("yes", "y"):
        new_operation = True
    else:
        new_operation = False