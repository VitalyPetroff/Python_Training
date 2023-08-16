# n = int(input())
# k = int(input())
n = 7
k = 5

lst = [1] * n
index = 0
while sum(lst) > 1:
    step = 0
    while step < k:
        if lst[index] == 1:
            step += 1
        index = (index + 1) % n
    lst[index] = 0
    while lst[index] == 0:
        index = (index + 1) % n
    print(*lst, sep='')
print('================')
print(index + 1)

