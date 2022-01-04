from random import uniform

def transfer_list_in_str(list_in: list) -> str:
  """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
      формирует из них единую строковую переменную разделяя значения запятой."""


  for i in my_list:
    a = [i]
    b = "".join(map(str, a))
    c = b.split(".")
    if int(c[1]) <= 9:
      c[1] = int(c[1]) * 10
    if int(c[0]) < 9:
      c[0] = '0' + c[0]

    print(f'{c[0]} руб {c[1]} коп', end=",")





my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)

my_list.sort()
print(f'По возрастанию', my_list)
print(f'По убыванию', my_list[::-1])





