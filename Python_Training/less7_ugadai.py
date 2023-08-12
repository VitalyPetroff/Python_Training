from random import randint


def is_valid(stroka):
    if stroka.isdigit():
        if 1 <= int(stroka) <= 100:
            return True
    return False


num = randint(1, 100)

print('Добро пожаловать в числовую угадайку')
attempt = 0
while True:
    stroka = input()
    if is_valid(stroka):
        answer = int(stroka)
        if answer == num:
            print('Вы угадали, поздравляем!')
            attempt += 1
            break
        elif answer > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            attempt += 1
        else:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        attempt += 1
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
