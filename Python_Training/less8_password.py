from random import choice


def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += choice(chars)
    return password


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

quantity = int(input('Какое количество паролей сгенерировать? Ваш ответ:'))
length = int(input('Какой длины сгенерировать пароль? Ваш ответ:'))
pass_digit = (True if input('Включать ли цифры в пароль (0123456789)? Ваш ответ:') == 'да' else False)
pass_upper = (True if input('Включать ли прописные буквы (ABCDEFGHIJKLMNOPQRSTUVWXYZ)? Ваш ответ:') == 'да' else False)
pass_lower = (True if input('Включать ли строчные буквы (abcdefghijklmnopqrstuvwxyz)? Ваш ответ:') == 'да' else False)
pass_symb = (True if input('Включать ли символы в пароль (!#$%&*+-=?@^_)? Ваш ответ:') == 'да' else False)
pass_exc = (True if input('Исключить ли неоднозначные символы (il1Lo0O)? Ваш ответ:') == 'да' else False)

chars = list()
if pass_digit:
    chars += digits
if pass_upper:
    chars += uppercase_letters
if pass_lower:
    chars += lowercase_letters
if pass_symb:
    chars += punctuation
if pass_exc:
    for el in 'il1Lo0O':
        while el in chars:
            chars.remove(el)

for _ in range(quantity):
    print(generate_password(length, chars))
