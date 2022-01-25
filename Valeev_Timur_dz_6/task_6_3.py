import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    :param path_users_file:
    :param path_hobby_file:
    :return:
    """
    names_hobby = {}
    with open(path_hobby_file, 'r', encoding='utf-8') as f1, \
            open(path_users_file, 'r', encoding='utf-8') as f2:
        for usr_name in f2:
            hobby = f1.readline().strip()
            usr_name = usr_name.strip()
            usr_name = usr_name.replace(',', ' ')
            if hobby:
                names_hobby.setdefault(usr_name, hobby.split(','))
            else:
                names_hobby.setdefault(usr_name, None)
        hobby = f1.readline()
        if hobby:
            sys.exit(1)

    return names_hobby


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
    for line in fw:
        print(line)

with open('task_6_3_result.json', 'r', encoding='utf-8') as fr:
    dict_from_file = json.load(fr)

print(dict_from_file)

