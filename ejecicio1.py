categoria = input("Categoría (A, B o C): ").upper()
monto = float(input("Monto de la compra: $"))

if categoria == "A":
    porcentaje = 0.20 if monto > 100000 else 0.10
elif categoria == "B":
    porcentaje = 0.15 if monto > 100000 else 0.05
elif categoria == "C":
    porcentaje = 0.05
else:
    porcentaje = None

if porcentaje is None:
    print("Categoría no válida.")
else:
    descuento = monto * porcentaje
    total = monto - descuento
    print(f"Descuento: ${descuento:,.0f}")
    print(f"Total a pagar: ${total:,.0f}")