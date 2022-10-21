import pandas as pd
from pandas import DataFrame
global df
df = pd.read_csv('table1.csv', encoding='cp1251')


def loading():
    print(df)
    return loading


def add():
    global df
    x1 = input('ID сотрудника: ')
    x2 = input('Фамилия: ')
    x3 = input('Имя: ')
    x4 = input('Отчество: ')
    x5 = input('Дата рождения: ')
    new_row = {'ID сотрудника': x1, 'Фамилия': x2,
               'Имя': x3, 'Отчество': x4, 'Дата рождения': x5}
    df = df.append(new_row, ignore_index=True)
    print(df)
    return add


def delete():
    global df
    x = int(input('Введите индекс строки: '))
    df = df.drop(index=[x])
    print(df)
    return delete


def export():
    df.to_csv('table2.csv', index=False)
