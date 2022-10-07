# 2. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
# Число 1 не имеет простых делителей и не является ни простым, ни составным числом.

number = int(input('Введите натуральное число N '))
lst = []
simplemult = 2
while number > 1:
    if number % simplemult == 0:
        lst.append(simplemult)
        number = number/simplemult
    else:
        simplemult += 1
print(lst)
