def menu():
    lst = {
        1: 'Просмотр справочника',
        2: 'Поиск контакта в справочнике',
        3: 'Экспорт контакта',
        4: 'Выход'}
    x = (int(input(f'{lst} \n Выберите следующее действие ')))
    return x
