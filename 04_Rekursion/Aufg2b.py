def fakultaet_rekursiv(n):
    if n <= 0:
        return 1
    else:
        return n * fakultaet_rekursiv(n - 1)

print(fakultaet_rekursiv(5))