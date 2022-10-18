import pandas as pd
from pandas import DataFrame


def viewing():
    df = pd.read_csv('teldir.csv', encoding='cp1251')
    print(df)
    return viewing


def search():
    import pandas as pd
    df = pd.read_csv('teldir.csv', encoding='cp1251', index_col='last_name')
    last_name = input('Введите фамилию ')
    line = df.loc[[f'{last_name}']]
    print(line)
    return search


def export():
    df = pd.read_csv('teldir.csv', encoding='cp1251', index_col='last_name')
    last_name = input('Введите фамилию ')
    line = df.loc[[f'{last_name}']]
    df = pd.DataFrame(line)
    df.to_csv(r'teldir2.csv', index=True)
    return export
