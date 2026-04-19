while True:
    numero = float(input("Ingresa un número: "))
    for i in range(1):
        if numero > 0:
            print("El número es positivo")
        elif numero < 0:
            print("El número es negativo")
        else:
            print("El número es cero")
    opcion = input("¿Deseas ingresar otro número? (s/n): ")
    while opcion != "s" and opcion != "n":
        opcion = input("Opción inválida. Ingresa s o n: ")
    if opcion == "n":
        print("Programa finalizado")
        break
