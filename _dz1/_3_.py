#Напишите программу, которая принимает на вход координаты точки (X и Y),
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)

abscissa = float(input('Введите значение оси "X" : '))
ordinate = float(input('Введите значение оси "Y" : '))
if abscissa > 0 < ordinate:
    print('1 четверть')
elif abscissa < 0 < ordinate:
    print('2 четверть')
elif abscissa < 0 > ordinate:
    print('3 четверть')
else:
    print('4 четверть')













