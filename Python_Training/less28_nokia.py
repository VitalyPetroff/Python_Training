klava = {1: '.,?!:',
         2: 'ABC',
         3: 'DEF',
         4: 'GHI',
         5: 'JKL',
         6: 'MNO',
         7: 'PQRS',
         8: 'TUV',
         9: 'WXYZ',
         0: ' '
         }

stroka = input().upper()
for symbol in stroka:
    for key, value in klava.items():
        if symbol in value:
            i = value.find(symbol) + 1
            # print(i)
            print(*([key] * i), sep='', end='')
