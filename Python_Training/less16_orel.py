lst = input().split('О')
mx = 0
for el in lst:
    mx = max(mx, len(el))
print(mx)