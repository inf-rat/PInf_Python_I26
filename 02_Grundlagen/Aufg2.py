# 2a
name = input("Bitte deinen Namen eingeben: ")
print(f"Guten Tag, {name}!")

# 2b
teststring = "PYTHON_IST_KEINE_INSEL"
liste = []
for i in range(0, len(teststring), 3):
    liste.append(teststring[i: i + 3])
    print(liste[-1])

