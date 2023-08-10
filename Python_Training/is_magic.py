# объявление функции
def is_magic(date):
    lst = date.split('.')
    if int(lst[0]) * int(lst[1]) == int(lst[2][2:]):
        return True
    else:
        return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))