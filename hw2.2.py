user_value = int(input('введіть 5-ти значне ціле число: '))
first_num = user_value // 10000
second_num = user_value // 1000 % 10 
third_num = user_value // 100 % 10 
fourth_num = user_value // 10 % 10
fifth_num = user_value % 10

print(fifth_num,fourth_num,third_num,second_num,first_num)
