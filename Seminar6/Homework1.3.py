# Задача: предложить улучшения кода для уже решённых задач (3-5 задач):
# С помощью использования: lambda, filter, map, zip, enumerate, list comprehension.
# -------------------------------------------------------------------------------------------------
# Найти сумму чисел списка стоящих на нечетной позиции
# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = 6
dictionary = dict(enumerate([3 * i + 1 for i in range(1, n + 1)], 1))
print(f"n = : {dictionary}")