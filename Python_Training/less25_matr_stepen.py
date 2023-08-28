def matrix_product(matrix_1, matrix_2):
    n, m = len(matrix_1), len(matrix_1[0])
    m, k = len(matrix_2), len(matrix_2[0])
    matrix_3 =[[0] * k for _ in range(n)]

    for i in range(n):
        for j in range(k):
            for c in range(m):
                matrix_3[i][j] += matrix_1[i][c] * matrix_2[c][j]
    return matrix_3


def matrix_degree(matrix_in, n):
    matrix_out = matrix_in
    if n > 1:
        for i in range(n - 1):
            matrix_out = matrix_product(matrix_out, matrix_in)
    else:
        return matrix_in
    return matrix_out


n = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(n)]
m = int(input())
matrix_res = matrix_degree(matrix, m)

for row in matrix_res:
    print(*row)
