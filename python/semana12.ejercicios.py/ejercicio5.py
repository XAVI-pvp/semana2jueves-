while True:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    operacion = input("Ingresa la operación (+, -, *, /): ")
    operaciones = ["+", "-", "*", "/"]
    valido = False
    for op in operaciones:
        if operacion == op:
            valido = True
    if valido:
        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Error: No se puede dividir entre cero")
                resultado = None
        if resultado is not None:
            print("Resultado:", resultado)
    else:
        print("Operación no válida. Usa +, -, * o /")
        opcion = input("¿Deseas hacer otra operación? (s/n): ")
    while opcion != "s" and opcion != "n":
        opcion = input("Opción inválida. Ingresa s o n: ")
    if opcion == "n":
        print("Programa finalizado")
        break
