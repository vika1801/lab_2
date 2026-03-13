# lab_2_13.py
# Вывод символов между скобками

s = input("Введите строку: ")

start = -1
end = -1

i = 0
while i < len(s):
    if s[i] == "(":
        start = i
    if s[i] == ")":
        end = i
        break
    i += 1

if start != -1 and end != -1 and end > start:
    i = start + 1
    while i < end:
        print(s[i], end="")
        i += 1
else:
    print("Скобки не найдены")