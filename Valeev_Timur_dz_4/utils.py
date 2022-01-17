import requests


def currency_rates(code: str) -> str | None:
    """возвращает курс валюты `code` по отношению к рублю"""
    # ваша реализация здесь
    res = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

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

    final_list = dict(zip(list_of_names, list_of_values))

    result_value = final_list.get(str(code))
    return result_value