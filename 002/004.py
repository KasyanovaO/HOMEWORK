# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Введите число элементов '))
list = []
for i in range(-N, N+1):
    list.append(i)
print(list)

path = 'file.txt'
data = open(path, 'r')
newdata = [int(line) for line in data]
print(newdata)
data.close()

mult = 1
for i in newdata:
    mult *= list[i]
print(mult)
