def encryption(language, text, step):
    lst1 = list(text)
    lst2 = list()
    for symbol in lst1:
        if symbol.isalpha():
            x = int(ord(symbol))
            if symbol.isupper():
                if language == 'рус':
                    lst2.append(chr((x - 1040 + step) % 32 + 1040))
                elif language == 'en':
                    lst2.append(chr((x - 65 + step) % 26 + 65))
            if symbol.islower():
                if language == 'рус':
                    lst2.append(chr((x - 1072 + step) % 32 + 1072))
                elif language == 'en':
                    lst2.append(chr((x - 97 + step) % 26 + 97))
        else:
            lst2.append(symbol)
    return ''.join(lst2)


stroka = input()
length = len(stroka)
result = ''
start, end = 0, 0
for i in range(length):
    if i == 0 and stroka[i].isalpha():  # первая буква слова в начале строки
        start = i
    if stroka[i].isalpha() and not stroka[i - 1].isalpha():   # первая буква слова в середине строки
        start = i
    if stroka[i].isalpha():
        if ((i < length - 1) and not stroka[i + 1].isalpha()) or i == length - 1:
            end = i + 1
            word = stroka[start:end]
            en_word = encryption('en', word, end - start)
            result += en_word
    if not stroka[i].isalpha():
        result += stroka[i]
print(result)
