def transformar_texto(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto[0].upper() + texto[1:].lower()
    else:
        return " no no mi rey inorrecto eso mejor pongase a aprender ingles"


palabra = input("Introduce una palabra: ")
numero = int(input("Introduce el número de transformación (1, 2 o 3): "))
resultado = transformar_texto(palabra, numero)
print("Resultado:", resultado)
