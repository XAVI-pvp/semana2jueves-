while True:
    numero = int(input("Ingresa un número del 1 al 7: "))
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    if numero >= 1 and numero <= 7:

        for i in range(len(dias)):
            if numero == i + 1:
                print(dias[i])
    else:
        print("Error: número fuera del rango (1 al 7)")
        opcion = input("¿Deseas ingresar otro número? (s/n): ")

    while opcion != "s" and opcion != "n":
        opcion = input("Opción inválida. Ingresa s o n: ")

    if opcion == "n":
        print("Programa finalizado")
        break
