"""
Задание 1
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
* до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
Примеры:
> duration = 53
53 сек
> duration = 153
2 мин 33 сек
> duration = 4153
1 час 9 мин 13 сек
> duration = 400153
4 дн 15 час 9 мин 13 сек
    Примечание: можете проверить себя здесь,
    подумайте, можно ли использовать цикл для проверки работы кода сразу для нескольких значений продолжительности,
    будет ли тут полезен список?
"""


def convert_time(duration: int) -> str:
    str_out = f"вы передали {duration} секунд и это равняется"
    return str_out
duration = int(input('Введите промежуток времени в секундах'))
result = convert_time(duration)
print(result)

duration_list = {}

if duration // 86400 > 0:
    day = duration//86400
    duration_list[day] = 'дн'
    duration = duration % 86400
if duration // 3600 > 0:
    hour = duration // 3600
    duration_list[hour] = 'час'
    duration = duration % 3600
if duration // 60 > 0:
    minute = duration // 60
    duration_list[minute] = 'мин'
    duration = duration % 60
if duration // 1 > 0:
    second = duration // 1
    duration_list[second] = 'сек'
    duration = duration % 1

for key in duration_list.keys():
    print(key, duration_list[key])
