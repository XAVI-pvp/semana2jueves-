def transformar_texto(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto[::-1]
    else:
        return "uyyy no papito no no tony star estari muy desepccionado de ver que no funciona con eso  "


texto = input("Ingresa un texto: ")
opcion = int(input("Elige una opción (1, 2 o 3): "))

resultado = transformar_texto(texto, opcion)

print("Resultado:", resultado)
