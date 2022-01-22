from typing import Any, Generator


def odd_nums(number: int) -> Generator[int, Any, None]:
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    #pass  # пишите свою реализацию здесь
    gen_num = (i for i in range(1, number + 1, 2))
    return gen_num


n = 25
generator = odd_nums(n)
for _ in range(1, n + 1, 2):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration