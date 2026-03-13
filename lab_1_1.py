# lab_1_1.py
# Считывание трех чисел и поиск минимального

try:
    first_number = float(input("Введите первое число: "))
    second_number = float(input("Введите второе число: "))
    third_number = float(input("Введите третье число: "))

    minimum = first_number

    if second_number < minimum:
        minimum = second_number

    if third_number < minimum:
        minimum = third_number

    print("Минимальное число:", minimum)

except ValueError:
    print("Ошибка: необходимо вводить только числа.")