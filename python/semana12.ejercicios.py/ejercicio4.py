while True:
    numero = int(input("Ingresa un número: "))
    for i in range(1):
        if numero % 2 == 0:
            print("El número es par")
        else:
            print("El número es impar")
    opcion = input("¿Deseas ingresar otro número? (s/n): ")
    while opcion != "s" and opcion != "n":
        opcion = input("Opción inválida. Ingresa s o n: ")
    if opcion == "n":
        print("Programa finalizado")
        break
