# объявление функции
def convert_to_python_case(text):
    lst = list(text)
    for i in range(len(lst)):
        if lst[i].isupper():
            lst[i] = lst[i].lower()
            if i != 0:
                lst.insert(i,'_')
            i += 1

    return ''.join(lst)

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))