# Aufg. 3a)
def maximum(a, b):
    if a > b:
        return a
    else:
        return b

zahl1 = int(input("Bitte Zahl 1 eingeben:"))
zahl2 = int(input("Bitte Zahl 2 eingeben:"))
print("Maximum: ", maximum(zahl1, zahl2))

# Aufg. 3b)
def fakultaet(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
print(fakultaet(5))

# Aufg. 3c)
from math import factorial
print(factorial(5))

# Aufg. 3d)
n = 10
for i in range(1, n + 1):
    if fakultaet(i) != factorial(i):
        print("Funktionen stimmen nicht überein für i =", i)
        break
print("Die Funktionen stimmen überein für alle natürlichen Zahlen bis ", n)