alphabet = 'abcdefgh'

koord = input()
x = alphabet.index(koord[0])
y = 8 - int(koord[1])

for i in range(8):
    for j in range(8):
        if (i == y - 2 or i == y + 2) and (j == x - 1 or j == x + 1) or (
                i == y - 1 or i == y + 1) and (j == x - 2 or j == x + 2):
            print('*', end=' ')
        elif i == y and j == x:
            print('N', end=' ')
        else:
            print('.', end=' ')
    print()
