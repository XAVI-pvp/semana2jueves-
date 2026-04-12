def transformar_texto(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto[::-1]
    else:
        return "No importa que seas el rojo más deslumbrante e intenso, si su color favorito es el azul (LO QUE QUIERO DECIR ES NO INCORRECTO)"


print("=== MENÚ ===")
print("1. Convertir a MAYÚSCULAS")
print("2. Convertir a minúsculas")
print("3. Invertir texto")

texto = input("Ingresa un texto: ")
opcion = int(input("Elige una opción (1, 2 o 3): "))

resultado = transformar_texto(texto, opcion)

print("Resultado:", resultado)
