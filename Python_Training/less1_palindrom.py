# объявление функции
def is_palindrome(text):
    text = text.lower()
    lst = list(text)
    i = 0
    while i < len(lst):
        if lst[i] in '.,!? -':
            del lst[i]
            continue
        i += 1
    for i in range(int(len(lst) / 2)):
        if lst[i] != lst[-i-1]:
            return False
    return True


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))