# 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

n = int(input('Введите число '))


def R(n):
    for i in range(1, n+1):
        R = (1 + 1 / n)**n
        return R


list = []
for e in range(1, n+1):
    list.append(R(e))
print(f'Cписок {list}')
print(f'Cумма {sum(list)}')
