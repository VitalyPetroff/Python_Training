n = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(n)]

status = 1

# проверка значений матрицы 1..n*n
numbers = list(range(1, n * n + 1))
matr = []
for row in matrix:
    matr.extend(row)
matr.sort()
if matr != numbers:
    status = 0

# проверка значений сумм
s = sum(matrix[0])
sum_diag_osn = 0
sum_diag_dop = 0

for i in range(n):
    if status:
        # проверка по строкам
        if sum(matrix[i]) != s:
            status = 0
            break

        # проверка по столбцам
        total = 0
        for j in range(n):
            total += matrix[j][i]
        if total != s:
            status = 0
            break

        # нахождение сумм по диагоналям
        sum_diag_osn += matrix[i][i]
        sum_diag_dop += matrix[i][n - 1 - i]

# проверка по диагоналям
if sum_diag_dop != s or sum_diag_osn != s:
    status = 0

if status:
    print('YES')
else:
    print('NO')
