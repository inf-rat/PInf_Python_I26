# 2a
name = input("Bitte deinen Namen eingeben: ")
print(f"Guten Tag, {name}!")

# Hilfestellung zu 2b
teststring = "PYTHON_IST_KEINE_INSEL"
for i in range(0, len(teststring), 3):
    print(teststring[i: i + 3])