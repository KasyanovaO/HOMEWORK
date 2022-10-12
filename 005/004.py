# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('inputdata.txt', 'r') as data:
    inputdata = data.read()
    encoding = ''
    i = 0
    while i < len(inputdata):
        count = 1
        while i + 1 < len(inputdata) and inputdata[i] == inputdata[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + inputdata[i]
        i = i + 1
with open('outputdata.txt', 'w') as data:
    data.write(str(encoding))

exit()
with open('outputdata.txt', 'r') as data:
    outputdata = data.read()
decoding = ''
i = 0
while len(outputdata[i: i + 2]) == 2:
    num, char = outputdata[i: i + 2]
    decoding += char * int(num)
    i = i + 2
with open('inputdata.txt', 'w') as data:
    data.write(str(decoding))
