def convert_name_extract(list_in: list) -> list:
  list_out = ["здесь должены оказаться результирующие строковые приветствия"]
  return list_out
list_1 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
list_out = []
for i in list_1:
  a = [i]
  b = " ".join(a)
  c = list(b.split())
  f = (c[-1])
  f = f.capitalize()
  list_out.append(f'Привет, {f}!')
print(list_out)