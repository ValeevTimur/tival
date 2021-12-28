"""
Задание 2
a) Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):

Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

Например, число `19 ^ 3 = 6859` будем включать в сумму, так как `6 + 8 + 5 + 9 = 28` – делится нацело на `7`.
Внимание: использовать только арифметические операции!

b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых
делится нацело на 7.

*c) Решить задачу под пунктом b, не создавая новый список. (если будете решать - либо создайте доп. функцию, либо
перепишите существующую sum_list_2)

list_1 = []
count = 1000
i = count
while i >= 1:
    list_1.append(i)
    i -= 1
list_1.reverse()

for i in list_1:
    if i % 2 == 0:
        list_1.remove(i)


print(list_1)



for number in range(1, 1000, 2):
    number = number ** 3
    if number % 7 == 0:
        print(number)
  """

#if i % 2 == 0 in list:

#if i % 2 == 0:
list_1 = [i**3 for i in range(1, 1000, 2)]
list_2 = []
list_3 = []

for i in list_1:
    a = 0
    s = 0
    p = i
    while i > 0:
        digit = i % 10
        a = a + digit
        i = i // 10

    if a % 7 == 0:
        s += p
        list_2.append(s)
print('Задание а) ', sum(list_2))


for t in list_2:
    t = t + 17
    m = 0
    n = 0
    z = t
    while i > 0:
        digit = i % 10
        m = m + digit
        t = t // 10

    if m % 7 == 0:
        t += z
        list_3.append(z)
print('Задание b) ', sum(list_3))









#for i, element in enumerate(list_2, start=1):
 #  print(f'индекс {i} значение {element}')





"""
day_sales = [1589.5, 2687.5, 5478.2, 1236.5, 4756.5]
idx = 0
total_sales = 0
while idx < len(day_sales):  # pre-condition
   total_sales = total_sales + day_sales[idx]
   idx = idx + 1
price_per_product = total_sales / len(day_sales)
print(price_per_product)  # 3149.6400000000003

"""





