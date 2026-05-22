# lab_2_13.py
# Вывод символов между скобками

try:
    text = input("Введите строку: ")

    start_index = -1
    end_index = -1

    i = 0
    while i < len(text):

        if text[i] == "(":
            start_index = i

        if text[i] == ")":
            end_index = i
            break

        i += 1

    if start_index != -1 and end_index != -1 and end_index > start_index:

        i = start_index + 1

        while i < end_index:
            print(text[i], end="")
            i += 1

    else:
        print("Ошибка: скобки не найдены.")

except Exception as error:
    print("Произошла ошибка:", error)