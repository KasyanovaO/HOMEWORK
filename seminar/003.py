# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# 
# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

lst =  ["1", "2fdhf", "zxc", "2qwe", "ertqwe"]
N = input("Введите число: ")

for item in lst:
    if N in item:
        print(f'Число {N} найдено в списке, в строке {item}')
        break



lst = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
N = input("Введите строку: ")
counter = 0
target_counter = 2

for i in range(len(lst)):
    if N == lst[i]:
        counter += 1
        if counter == target_counter:
            print(f'Строка {N} найдена в списке. Ее {counter} нахождение в списке под индексом {i}')



