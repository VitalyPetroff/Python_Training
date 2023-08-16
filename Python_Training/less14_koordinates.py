n = int(input())
lst = list()
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
for _ in range(n):
    lst.append(input().split())
for el in lst:
    x = float(el[0])
    y = float(el[1])
    if x > 0:
        if y > 0:
            count_1 += 1
        elif y < 0:
            count_4 += 1
    if x < 0:
        if y > 0:
            count_2 += 1
        elif y < 0:
            count_3 += 1
print('Первая четверть:', count_1)
print('Вторая четверть:', count_2)
print('Третья четверть:', count_3)
print('Четвертая четверть:', count_4)