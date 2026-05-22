#lab_3_13.py
#Работа со списком

import random

try:
    n = int(input("Введите размер массива: "))

    if n <= 0:
        print("Размер массива должен быть больше нуля.")
        exit()

    numbers = []

    for i in range(n):
        numbers.append(random.randint(0, 30))

    print("Исходный массив:", numbers)

    found = False

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):

            if numbers[i] == numbers[j]:
                print("Повторяющиеся элементы:", numbers[i],
                      "индексы:", i, j)
                found = True

    if not found:
        print("Повторяющихся элементов нет.")

    for i in range(len(numbers)):

        if numbers[i] < 15:
            numbers[i] = numbers[i] * 2

    print("Измененный массив:", numbers)

except ValueError:
    print("Ошибка: необходимо вводить целое число.")

except Exception as error:
    print("Произошла ошибка:", error)