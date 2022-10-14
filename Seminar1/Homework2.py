# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
def isTrue(x, y, z):
    if not (x or y or z) == (not x) and (not y) and (not z):
        return 'ИСТИННО'
    return 'ЛОЖНО'

print('Проверка истинности утверждения ¬(X v Y v Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат')
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'При X = {x}, Y = {y}, Z = {z}) - {isTrue(x, y, z)}')
            