stroka = input()
list_of_words = stroka.split()
result = ''

for word in list_of_words:  # проходим по каждому элементу списка
    shift = sum([int(s.isalpha()) for s in word])  # длина слова

    new_word = ''
    for ch in word:  # проходим по каждому символу слова
        if ch.isalpha():  # проверяем символ - это буква
            if ch.islower():  # это строчная буква?
                ch = chr((ord(ch) - 97 + shift) % 26 + 97)
            else:  # это прописная буква
                ch = chr((ord(ch) - 65 + shift) % 26 + 65)
        new_word += ch

    result += new_word + ' '
print(result)