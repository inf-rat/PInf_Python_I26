def laenge(lst):
    if lst == []:
        return 0
    else:
        lst.pop()
        return 1 + laenge(lst)

print(laenge([1, 2, 3]))