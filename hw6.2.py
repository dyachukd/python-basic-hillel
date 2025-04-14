seconds = int(input("Введіть кількість секунд (0 <= x < 8640000): "))

if 0 <= seconds < 8640000:
    days = seconds // 86400
    remaining = seconds % 86400

    hours = remaining // 3600
    remaining = remaining % 3600

    minutes = remaining // 60
    secs = remaining % 60

    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif days % 10 in [2, 3, 4] and not (12 <= days % 100 <= 14):
        day_word = "дні"
    else:
        day_word = "днів"

    hours_str = str(hours).zfill(2)
    minutes_str = str(minutes).zfill(2)
    secs_str = str(secs).zfill(2)

    print(f"{days} {day_word}, {hours_str}:{minutes_str}:{secs_str}")
else:
    print("Число повинно бути від 0 до 8 639 999 включно.")
