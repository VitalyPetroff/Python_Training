n, m = [int(el) for el in input().split()]
matrix_1 = [[int(el) for el in input().split()] for _ in range(n)]
input()
m, k = [int(el) for el in input().split()]
matrix_2 = [[int(el) for el in input().split()] for _ in range(m)]

matrix_3 = [[0] * k for i in range(n)]

for i in range(n): # индексы строк в новой матрице
    for j in range(k):  # индексы столбцов в новой матрице
        for a in range(m):  # индексы столбцов в первой матрице
            matrix_3[i][j] += matrix_1[i][a] * matrix_2[a][j]

for row in matrix_3:
    print(*row)