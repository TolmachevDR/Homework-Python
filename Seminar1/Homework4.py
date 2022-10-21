## Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def check_quater(number):
    if number == 1:
        print(f'Диапазон координат точек в первой четверти x > 0 и y > 0')
    elif number == 2:
        print(f'Диапазон координат точек во второй четверти x < 0 и y > 0')
    elif number == 3:
        print(f'Диапазон координат точек в третьей четверти x < 0 и y < 0')
    elif number == 4:
        print(f'Диапазон координат точек в четвертой четверти x > 0 и y < 0')
    else:
        print(f'Диапазон не найден')

number = int(input('Введите номер четверти '))
check_quater(number)