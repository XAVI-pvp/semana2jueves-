while True:
    a = float(input("Ingresa el lado A: "))
    b = float(input("Ingresa el lado B: "))
    c = float(input("Ingresa el lado C: "))
    for i in range(1):
        if a == b and b == c:
            print("El triángulo es equilátero")
        elif a == b or a == c or b == c:
            print("El triángulo es isósceles")
        else:
            print("El triángulo es escaleno")
    opcion = input("¿Deseas ingresar otros lados? (s/n): ")
    while opcion != "s" and opcion != "n":
        opcion = input("Opción inválida. Ingresa s o n: ")
    if opcion == "n":
        print("Programa finalizado")
        break
