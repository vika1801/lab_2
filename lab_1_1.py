# lab_1_1.py
# Считывание трех чисел и поиск минимального

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

minimum = a

if b < minimum:
    minimum = b

if c < minimum:
    minimum = c

print("Минимальное число:", minimum) 