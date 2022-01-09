def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    str_out = dict_numbers.get(value)
    return str_out

dict_numbers = {
    "one": 'один',
    "two": 'два',
    "tree": 'три',
    "four": 'четыре',
    "five": 'пять',
    "six": 'шесть',
    "seven": 'семь',
    "eight": 'восемь',
    "nine": 'девять',
    "ten": 'десять'
}

print(dict_numbers)
print(num_translate("one"))
print(num_translate("two"))
print(num_translate("tree"))
print(num_translate("four"))
print(num_translate("five"))
print(num_translate("six"))
print(num_translate("seven"))
print(num_translate("eight"))
print(num_translate("nine"))
print(num_translate("ten"))
print(num_translate("eleven"))