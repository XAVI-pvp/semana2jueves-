num = int(input("Ingresa un número (-1 para salir): "))

while num != -1:
    print(f"\nTabla del {num} (solo resultados mayores a 20):")
    for i in range(1, 11):
        resultado = num * i

        if resultado > 20:
            print(f"{num} x {i} = {resultado}")
    num = int(input("\nIngresa otro número (-1 para salir): "))
print("Programa finalizado.")
