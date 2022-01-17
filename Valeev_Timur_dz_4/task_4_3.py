import requests
import datetime

def currency_rates_adv(code: str) -> str | None:
    """возвращает курс валюты `code` по отношению к рублю"""
    # ваша реализация здесь
    res = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

    #Проверка ответа сервера
    #if res:
    #    print('Response OK')
    #else:
    #    print('Response Failed')

    res_in_txt = res.text
    split_1 = res_in_txt.split('<CharCode>')

    split_2 = split_1[1::]

    list_of_names = []
    for i in split_2:
        b = i[0:3:]
        list_of_names.append(b)

    split_3 = res_in_txt.split('<Value>')
    split_4 = split_3[1::]

    list_of_values = []
    for d in split_4:
        c = d[0:7:]
        p = float(c.replace(',', '.'))

        list_of_values.append(p)



    split_5 = res_in_txt.split('<ValCurs Date="')

    split_6 = split_5[1]
    split_7 = split_6[0:10:]


    year = split_7[6::]
    month = split_7[3:5:]
    if month[0] != 1:
        month = month[1::]
    day = split_7[:2:]
    if day[0] != 1:
        day = day[1::]

    date_value = datetime.date(int(year), int(month), int(day))


    final_list = dict(zip(list_of_names, list_of_values))

    kurs = final_list.get(str(code))
    return kurs, date_value





kurs, date_value = currency_rates_adv("JPY")

empty = bool(not kurs and not date_value)
if not empty and not isinstance(kurs, float):
    raise TypeError("Неверный тип данных у курса")
if not empty and not isinstance(date_value, datetime.date):
    raise TypeError("Неверный тип данных у даты")
print(kurs, date_value)
