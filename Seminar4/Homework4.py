#Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов(значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# Пример k=2 => 2*x^2+4*x = 0

from random import*
from math import*

a = [randint(0,100) for i in range(1,10)]
print(a)

f = open('file.txt','r')
for i in a:
  f.write(f'2*pow(2,{i})+4*x=0\n')
  