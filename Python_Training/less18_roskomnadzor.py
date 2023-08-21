stroka = input() + ' запретил букву'
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
for letter in alphabet:
    next_letter = stroka.find(letter)
    if next_letter != -1:
        print(stroka.strip(), letter)
        lst = stroka.split(letter)
        stroka = ''.join(lst)
        while '  ' in stroka:
            stroka = stroka.replace('  ', ' ')