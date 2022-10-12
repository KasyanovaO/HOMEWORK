# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random

print(f'Условие игры: На столе лежит 2021 конфета. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход')
number_candies = 2021
take_max = 28
player1 = input('Введите имя игрока ')
player2 = 'Компьютер'
turn = random.randint(0, 2)
if turn:
    print(f'{player1} ходит первым!')
else:
    print(f'{player2} ходит первым!')
while number_candies > 28:
    if turn:
        take = int(input(f'{player1}, введите количество конфет от 1 до 28: '))
        while take < 1 or take > 28:
            take = int(input(f'{player1}, введите корректное количество '))
        number_candies -= take
        turn = False
        print(
            f'Игрок {player1}, взял {take} конфет, всего осталось {number_candies} конфет')
    else:
        if number_candies == 2021:
            take = number_candies % 29
        elif number_candies < 2021:
            take = random.randint(1, 28)
        number_candies -= take
        turn = True
        print(f'{player2}, взял {take} конфет, всего осталось {number_candies} конфет')
if turn:
    print(f'Осталось {number_candies}, победил {player1}')
else:
    print(f'Осталось {number_candies}, победил {player2}')
