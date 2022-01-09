def thesaurus(value: str) -> str:
    list_of_names.append(value)
    b = value[0]
    dict_thesaurus.append(b)

    a = dict(zip(dict_thesaurus, list_of_names))
    return a

list_of_names = []
dict_thesaurus = []
dict_final = {}





print(thesaurus("Иван"))
print(thesaurus("Владимир"))
print(thesaurus("Эдуард"))
print(thesaurus("Константин"))
print(thesaurus("Николай"))
print(thesaurus("Эмиль"))
print(thesaurus("Виталий"))
print(thesaurus("Петр"))
print(thesaurus("Григорий"))
print(thesaurus("Ярослав"))
print(thesaurus("Яков"))
print(thesaurus("Дмитрий"))
