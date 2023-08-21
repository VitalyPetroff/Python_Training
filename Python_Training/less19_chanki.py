def chunked(lst_in, n):
    k = 0
    lst_out = []
    while k < len(lst_in):
        lst_out.append(lst_in[k : k + n])
        k += n
    return lst_out


lst = input().split()
n = int(input())

print(chunked(lst, n))
