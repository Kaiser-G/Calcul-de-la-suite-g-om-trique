a = 1
r = 2
n = 30

# Calculer la somme des n premiers termes
S_n = 0
for i in range(n):
    S_n += a * r ** i

print("La somme des 30 premiers termes est :", S_n)
