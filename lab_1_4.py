# lab_1_4.py
# Сумма и количество чисел последовательности

total_sum = 0
numbers_count = 0

print("Введите целые числа. Для завершения введите 0.")

while True:

    try:
        number = int(input())

        if number == 0:
            break

        total_sum += number
        numbers_count += 1

    except ValueError:
        print("Ошибка: необходимо вводить целое число.")

print("Сумма:", total_sum)
print("Количество:", numbers_count)