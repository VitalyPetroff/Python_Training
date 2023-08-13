import random


def get_word(lst):
    return random.choice(lst).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)

    alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЫЭЮЯ'
    while not guessed:
        answer = input('Введите букву или полностью слово: ').upper()
        if len(answer) == 1:    # введен символ
            if answer in alphabet:  # введенный символ - это буква
                if answer in guessed_letters:
                    print('Буква уже вводилась. Введите новую букву')
                elif answer in word:
                    guessed_letters.append(answer)  # дополняем список названных букв
                    length = 0
                    for el in word:
                        if el in guessed_letters:
                            length += 1
                            print(el, end='')
                            if length == len(word):
                                print('\nПоздравляем, вы угадали слово! Вы победили!')
                                guessed = True
                        else:
                            print('_', end='')
                    print()
                else:
                    guessed_letters.append(answer)
                    tries -= 1
                    print(display_hangman(tries))
                    if tries == 0:
                        print(word)
                        break
            else:
                print('Введенный символ не буква, введите букву')
        else:
            if answer != word:
                tries -= 1
                print(display_hangman(tries))
                if tries == 0:
                    print(word)
                    break
            else:
                print('Поздравляем, вы угадали слово! Вы победили!')
                guessed = True

word_list = ['виселица', 'небосвод', 'ожерелье', 'травалатор', 'многоточие', 'лестница']

while True:
    ans = input('Сыграем в игру "Виселица"? (да/нет)')
    if ans == 'да':
        play(get_word(word_list))
    else:
        break