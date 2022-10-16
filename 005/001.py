# Напишите программу, удаляющую из текста все слова, содержащие "абв".

import xdrlib


s = 'напишите программу, удаляющую из текста все слова, содержащие "абв" автобус'.split()
print(s)
result = filter(lambda x: 'а' not in x and 'б' not in x and 'в' not in x, s)
print(*result)
