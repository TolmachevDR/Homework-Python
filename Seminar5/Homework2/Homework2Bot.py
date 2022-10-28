#Создайте программу для игры с конфетами человек против бота.

from random import randint

# Ввод конфет и проверка на коректность ввода, указанном в запросе.
def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

# Вывод результата действий совершенного хода
def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

# Ввод имени участника
player1 = input("Введите имя первого игрока: ")
player2 = "Bot"


# Заданное колличество конфет на столе
value = 2021
print(f"Колличество конфет на столе: {value}")

# Флаг очередности
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

# Счетчик конфет у каждого игрока
counter1 = 0
counter2 = 0

# Проверка оставшегося колличества конфет на столе
while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = randint(1,29)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

# Вывод победителя в терминал
if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
