# Andrey Malakanov
# Skillbox PythonBasic

print('Задача 7. Костя хочет выигрывать')

# После игры в кубики Костя захотел немного изучить работу игровых автоматов,
# а заодно математику и теорию вероятностей.
# Но ему нужно с чего-то начать:
# написать программу, которая поможет выявить закономерности в комбинациях чисел на автомате.
 
# Даны три целых числа.
# Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел:
# 3 (если все совпадают),
# 2 (если два совпадает) или 0 (если все числа различны).

first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
third_num = int(input('Введите третье число: '))
if (first_num == second_num) and (first_num == third_num):
  print(3)
elif (first_num == second_num) or (first_num == third_num) or (second_num == third_num):
  print(2)
else:
  print(0)