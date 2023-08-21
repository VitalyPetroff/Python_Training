def podspiski(lst_in):
    lst_out = list()
    length_in = len(lst_in)
    for length in range(1, length_in + 1):
        index = 0
        while (index + length) <= length_in:
            lst_out.append(lst_in[index : index + length])
            index += 1
    lst_out.insert(0, [])
    return lst_out


lst = input().split()
print(podspiski(lst))