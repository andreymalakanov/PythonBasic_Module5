# Andrey Malakanov
# Skillbox PythonBasic

print('Задача 1. Калькулятор опыта')

# Андрей любит играть в компьютерные игры.
# И в один прекрасный день у него появилась классная идея для сюжета своей игры.
# Чтобы воплотить её в жизнь,
# он начал изучать программирование и геймдизайн.
# Начал он с главного героя и его системы прокачки.
 
# Напишите программу,
# которая определяет уровень персонажа в компьютерной игре.
# Пользователь вводит число «очков опыта», а программа вычисляет уровень.
# Новый уровень даётся при достижении 1000, 2500 и 5000 «очков опыта».
# Начальный уровень равен 1.
 
# Пример:
# Введите количество опыта: 6000
# Ваш уровень: 4
 
# Пример 2:
# Введите количество опыта: 2000
# Ваш уровень: 2

skill = int(input('Введите количество опыта: '))
level = 0
if skill < 1000:
  level += 1
elif (skill >= 1000) and (skill < 2500):
  level += 2
elif (skill >= 2500) and (skill < 5000):
  level += 3
else:
  level +=4
print('Ваш уровень:', level)