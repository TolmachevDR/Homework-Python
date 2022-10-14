# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random

def funk4(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(-n, n))
    return arr

def sum_arr(m,arr):
    s = 0
    split_m = m.split(',')
    for i in split_m:
        s +=arr[int(i)-1]
    return s

n = int(input("Ведите величину размера массива: "))
array = funk4(n)
print(array)
m = input("Введите номера позиций в массиве через запятую чтобы суммировать их: ")
print(sum_arr(m,array))