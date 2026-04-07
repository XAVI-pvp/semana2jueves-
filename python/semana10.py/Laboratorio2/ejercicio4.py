def transformar_lista(lista_palabras, opcion):
    resultado = []

    for palabra in lista_palabras:
        if opcion == 1:
            resultado.append(palabra.upper())
        elif opcion == 2:
            resultado.append(palabra.lower())
        elif opcion == 3:
            resultado.append(palabra[::-1])
        else:
            return "¡No puedes pasar!"

    return resultado


entrada = input("Escribe palabras separadas por coma (ej: hola,mundo,python): ")
opcion = int(input("Elige una opción (1, 2 o 3): "))


lista_palabras = entrada.split(",")

resultado = transformar_lista(lista_palabras, opcion)

print("Resultado:", resultado)
