# объявление функции
def is_palindrome(text):
    text = text.lower()
    lst = text.split()
    for el in lst:
        while '.' in el:
            lst.remove('.')
        while ',' in el:
            lst.remove(',')
        while '!' in el:
            lst.remove('!')
        while '?' in el:
            lst.remove('?')
        while '-' in el:
            lst.remove('-')
    print(*lst)
    length = len(lst)
    len_2 = 0
    if length % 2 == 0:
        len_2 = int(length / 2)
    else:
        len_2 = int(length / 2)
    for i in range(len_2):
        if lst[i] != lst[-i]:
            return False
    return True


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))