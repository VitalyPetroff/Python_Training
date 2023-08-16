n = int(input())
k = int(input())

lst = [1] * n
index = 0
while sum(lst) > 1:
    step = 0
    while step < k:
        if lst[index] == 1:
            step += 1
            if step == k:
                lst[index] = 0
        index = (index + 1) % n
print(lst.index(1) + 1)

