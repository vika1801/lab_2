# lab_1_3.py
# Вывод последовательности (1*m ... 10*m)

try:
    m = float(input("Введите число m: "))

    for i in range(1, 11):
        result = i * m
        print(result)

except ValueError:
    print("Ошибка: необходимо вводить число.")
