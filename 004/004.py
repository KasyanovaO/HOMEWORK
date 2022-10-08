# 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import numpy
from random import randint
from sympy import Symbol, expand

k = int(input("Введите натуральную степень k = "))
ratios = [randint(0, 10) for i in range(k+1)]
print(ratios)
p = numpy.poly1d(ratios)
x = Symbol('x')
with open('file5.txt', 'w') as data:
    data.write(str(expand(p(x))).replace('**', '^'))
