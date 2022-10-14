## Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
## Пример:
## - 6 -> да
## - 7 -> да
## - 1 -> нет

print("Введите номер дня недели: ")
dayNumber = int(input("Введите номер дня недели: "))

def DayRecognition(dayNumber):
if dayNumber == 6 or dayNumber == 7:
    print("Этот день выходной!")
elif dayNumber > 0 and dayNumber < 6:
    print("Это будний день!")
elif dayNumber < 1 or dayNumber > 7:
    print("Вы ввели неверное число! Попробуйте ввести снова!")

DayRecognition(dayNumber)
