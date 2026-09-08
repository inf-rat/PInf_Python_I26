def n_mal_hallo(n):
    if n > 0:
        print("Hallo!")
        n_mal_hallo(n - 1)

n_mal_hallo(3)