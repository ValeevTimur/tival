from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    pass  # Ваша реализация здесь
    #print(line)
    adr = line.split(' - - ')[0]
    get_str = line.split('] "')[1].split(' /')[0]
    path_str = line.split(' /')[1].split(' HTTP')[0]
    return adr, get_str, path_str
    #return  # верните кортеж значений <remote_addr>, <request_type>, <requested_resource>


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        #print(line)
        list_out.append(get_parse_attrs(line))

pprint(list_out)