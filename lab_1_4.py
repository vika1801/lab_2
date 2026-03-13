# lab_1_4.py
# Сумма и количество чисел последовательности

total = 0
count = 0

print("Введите целые числа. Для завершения введите 0.")

num = int(input())

while num != 0:
    total = total + num
    count = count + 1
    num = int(input())

print("Сумма:", total)
print("Количество:", count)