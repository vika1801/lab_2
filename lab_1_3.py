# lab_1_3.py
# Вывод последовательности (1*m ... 10*m)

m = float(input("Введите число m: "))

for i in range(1, 11):
    value = i * m
    print(value)