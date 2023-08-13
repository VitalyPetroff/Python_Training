def caesar_cryption(language, text, direction, step):
    step = int(step)
    if direction == '0':
        stroka = encryption(language, text, step)
        return stroka
    if direction == '1':
        stroka = dencryption(language, text, step)
        return stroka



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


def dencryption(language, text, step):
    lst1 = list(text)
    lst2 = list()
    for symbol in lst1:
        if symbol.isalpha():
            x = int(ord(symbol))
            if symbol.isupper():
                if language == 'рус':
                    lst2.append(chr((x - 1040 - step) % 32 + 1040))
                elif language == 'en':
                    lst2.append(chr((x - 65 - step) % 26 + 65))
            if symbol.islower():
                if language == 'рус':
                    lst2.append(chr((x - 1072 - step) % 32 + 1072))
                elif language == 'en':
                    lst2.append(chr((x - 97 - step) % 26 + 97))
        else:
            lst2.append(symbol)
    return ''.join(lst2)


# direction = input('Шифрование (0), дешифрование (1) ? ')
# language = input('Язык текста (рус/en)? ')
# step = input('Шаг сдвига? ')

for i in range(0, 26):
    print(caesar_cryption('en', 'Hawnj pk swhg xabkna ukq nqj.', '1', str(i)))
