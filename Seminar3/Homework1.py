# Задайте список из нескольких чисел. Напишите программу, которая 
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

s = input("Задайте список из нескольких целых чисел через пробел:   ").split()
print(s)
sum = 0
for i in range(1, len(s), 2):
        sum += int(s[i])
print(f'Cуммa элементов списка, стоящих на нечётных позициях: {sum}')
