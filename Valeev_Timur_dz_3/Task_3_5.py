from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]



def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    # Создаем копии списков чтобы не изменять оригинальные списки
    nouns_copy = nouns.copy()
    adverbs_copy = adverbs.copy()
    adjectives_copy = adjectives.copy()
    list_out = []
    n = 1
    # Цикл перебора count который записывает значения в список list_out
    while count >= n:
        # Определяем случайное значение в исходных списках
        rnd_nouns = choice(nouns_copy)
        # Очищаем копии списка от уже использованных значений, чтобы избежать повторов
        nouns_copy.remove(rnd_nouns)
        rnd_adverbs = choice(adverbs_copy)
        adverbs_copy.remove(rnd_adverbs)
        rnd_adjectives = choice(adjectives_copy)
        adjectives_copy.remove(rnd_adjectives)
        # собираем строку
        a = rnd_nouns + ' ' + rnd_adverbs + ' ' + rnd_adjectives
        list_out.append(a)
        n = n + 1

    return list_out

print(get_jokes(2))
print(get_jokes(3))
# Для данной длины списка максимальное значение count = 5, если убрать условие очистки списка, то count может быть любой
print(get_jokes(5))
