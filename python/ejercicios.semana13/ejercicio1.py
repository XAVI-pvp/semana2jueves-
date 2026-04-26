n = int(input("Ingresa un número (0 para salir): "))

while n != 0:
    print("Números pares del 1 al", n, ":")

    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)

    print()

    n = int(input("Ingresa otro número (0 para salir): "))

print("Programa finalizado.")
