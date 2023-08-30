import time
n, m = [int(el) for el in input().split()]
start_time = time.time()
step_x, step_y = m, n
matrix = [[0] * m for _ in range(n)]
k = n * m
num = 1
x_start, y_start = 0, 0

while True:
    # по столбцам вправо
    for x in range(x_start, x_start + step_x):
        matrix[y_start][x] = num
        num += 1
    step_x -= 1
    if num > k:
        break
    x_start += step_x
    y_start += 1

    # по строкам вниз
    for y in range(y_start, y_start + step_y - 1):
        matrix[y][x_start] = num
        num += 1
    step_y -= 1
    if num > k:
        break
    y_start += step_y - 1
    x_start -= 1

    # по столбцам влево
    for x in range(x_start, x_start - step_x, -1):
        matrix[y_start][x] = num
        num += 1
    step_x -= 1
    if num > k:
        break
    x_start -= step_x
    y_start -= 1

    # по строкам вверх
    for y in range(y_start, y_start - step_y + 1, -1):
        matrix[y][x_start] = num
        num += 1
    step_y -= 1
    if num > k:
        break
    y_start = y_start - step_y + 1
    x_start += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
end_time = time.time()
print(end_time - start_time)