while True:
    monto = float(input("Ingresa el monto de la compra: "))

    if monto > 100:
        descuento = monto * 0.20
        total = monto - descuento
        porcentaje = 20
    elif monto >= 50:
        descuento = monto * 0.10
        total = monto - descuento
        porcentaje = 10
    else:
        descuento = 0
        total = monto
        porcentaje = 0
        print("\n--- Detalle de la compra ---")
    for i in range(1):
        print("Monto original:", monto)
        print("Descuento aplicado:", porcentaje, "%")
        print("Total a pagar:", total)
