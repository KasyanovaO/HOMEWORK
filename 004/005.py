# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


import sympy

with open(str('file1.txt'), 'r') as data1, open(str('file2.txt'), 'r') as data2:
    file1 = data1.read()
    file2 = data2.read()

polynomial1 = sympy.polys.polytools.poly_from_expr(file1)[0]
polynomial2 = sympy.polys.polytools.poly_from_expr(file2)[0]

polynomialsum = polynomial1+polynomial2

with open('file3.txt', 'w') as data:
    data.write(str(polynomialsum.as_expr()).replace('**', '^'))
