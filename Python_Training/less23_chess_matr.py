n, m = [int(el) for el in input().split()]
matrix = []

for i in range(n):
    matrix.append([])
    for j in range(m):
        if (i + j) % 2 == 0:
            matrix[i].append('.')
        else:
            matrix[i].append('*')

for row in matrix:
    print(*row)
