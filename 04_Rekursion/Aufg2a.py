def summe_rekursiv(n):
    # Basisfall:
    if n == 0:
        return 0
    # Rekursionsanweisung:
    elif n > 0:
        return n + summe_rekursiv(n - 1)
    # Fehlermeldung für negative Werte:
    else:
        print("Summe ist nur für ganze Zahlen definiert.")

print(summe_rekursiv(5))