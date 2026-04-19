while True:
    año = int(input("Ingresa un año: "))
    for i in range(1):
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")
    opcion = input("¿Deseas ingresar otro año? (s/n): ")
    while opcion != "s" and opcion != "n":
        opcion = input("Opción inválida. Ingresa s o n: ")
    if opcion == "n":
        print("Programa finalizado")
        break
