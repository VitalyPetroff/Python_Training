anton = 'anton'
n = int(input())
num_str = []
for i in range(n):
    stroka = input()
    ind_l = 0
    count = 0
    for j in range(len(anton)):
        ind = stroka.find(anton[j], ind_l)  # индекс символа в строке
        if ind == -1:  # если символа в строке нету
            break
        else:  # если символ в строке есть
            ind_l = ind + 1
            count += 1
    if count == 5:
        num_str.append(i + 1)
print(*num_str)