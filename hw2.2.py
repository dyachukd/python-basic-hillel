user_value = int(input('введіть 5-ти значне ціле число: '))
first_digit= user_value // 10000
second_digit = user_value // 1000 % 10 
third_digit = user_value // 100 % 10 
fourth_digit = user_value // 10 % 10
fifth_digit = user_value % 10
reversed_number = fifth_digit * 10000 + fourth_digit * 1000 + third_digit * 100 + second_digit * 10 + first_digit
print(reversed_number)
