elements = ['камень', 'ножницы', 'бумага', 'ящерица', 'спок']
winning = [[1, 3], [2, 3], [0, 4], [2, 4], [0, 1]]
index_1 = elements.index(input())
index_2 = elements.index(input())
if index_1 == index_2:
    print('ничья')
else:
    flag = False
    for j in range(2):
        if winning[index_1][j] == index_2:
            flag = True
            break
    if flag:
        print('Тимур')
    else:
        print('Руслан')
