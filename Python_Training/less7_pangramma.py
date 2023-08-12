# объявление функции
def is_pangram(text):
        lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for el in lst:
            if el not in text.lower():
                return False
        return True


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))