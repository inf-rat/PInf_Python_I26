def summe_rekursiv(n):
    # Basisfall: Summe für n = 0 ist 0
    # Rekursionsanweisung:
    # Für n > 0 ist die Summe n + summe_rekursiv(n - 1)
    if n == 0:
        return 0
    elif n > 0:
        return n + summe_rekursiv(n - 1)
    else:
        print("Summe ist nur für ganze Zahlen definiert.")

print(summe_rekursiv(-4))