list_1 = [i**3 for i in range(1, 1000, 2)]
list_2 = []
list_3 = [i+17 for i in list_1]
print(list_3)
for i in list_3:
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