a = 15 / 3
b = 15 * 3
c = 15 // 2
d = 15 ** 2
list = [a, b, c, d]
n = 1
for i in list:
  print(f'Результат выражения {n} = {i}')
  print(f'Тип выражения {n}:')
  print(type(i))
  n += 1
