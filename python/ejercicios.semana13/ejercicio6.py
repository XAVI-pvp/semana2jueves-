# Programa: Números primos en un rango

while True:
    n = int(input("Ingresa un número (0 para salir): "))

    if n == 0:
        print("Programa finalizado.")
        break

    print("Números primos del 1 al", n, ":")

    for num in range(2, n + 1):
        contador = 0

        for i in range(1, num + 1):
            if num % i == 0:
                contador += 1

        if contador == 2:
            print(num)
