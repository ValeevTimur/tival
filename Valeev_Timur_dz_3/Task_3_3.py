"""
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся
с соответствующей буквы.

Например:

$ thesaurus("Иван", "Мария", "Петр", "Илья")
{
"И": ["Иван", "Илья"],
"М": ["Мария"],
"П": ["Петр"]
}

Подумайте:
* полезен ли будет вам оператор распаковки?
* Как поступить, если потребуется сортировка по ключам?
* Можно ли использовать словарь в этом случае?
"""


def thesaurus(value: str) -> str:
    list_of_names.append(value)
    b = value[0]
    dict_thesaurus.append(b)




    #c = sorted(clear_dict_thesaurus)




    a = dict(zip(dict_thesaurus, list_of_names))
    return a










    """
     b = value[0]
    a = {b: [value]}
    dict_final.update(a)
    return dict_final
    
    
    _________________________________
    
    
    for key in a.keys():

        print(a)
        if b == a.keys():
            temp_list = []
            a[key] = temp_list
            temp_list.append(value)
            print(a)
    """



    """
    if key != dict_final.keys():
        list_of_names.append(value)
        print(list_of_names)
        dict_thesaurus[key] = list_of_names
        dict_final.update(dict_thesaurus)
    else:
        for key in dict_final:
            if key == dict_final.keys():
                dict_thesaurus[key] = list_of_names.append(value)
                dict_final.update(dict_thesaurus)
        #print('Это функция:', dict_final)
    """


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
