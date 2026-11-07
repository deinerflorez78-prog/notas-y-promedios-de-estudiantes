numeros = [14, 25, 42, 31, 19, 8, 50, 73, 11, 22]

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Pares:", pares)
print("Cantidad de pares:", len(pares))

print("Impares:", impares)
print("Cantidad de impares:", len(impares))