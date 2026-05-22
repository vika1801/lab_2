# lab_1_2.py
# Вывод чисел из диапазона [1, 50]

try:
    first_number = float(input("Введите первое число: "))
    second_number = float(input("Введите второе число: "))
    third_number = float(input("Введите третье число: "))

    if 1 <= first_number <= 50:
        print(first_number)

    if 1 <= second_number <= 50:
        print(second_number)

    if 1 <= third_number <= 50:
        print(third_number)

except ValueError:
    print("Ошибка: необходимо вводить только числа.")