def transformar_texto(texto, opcion):

    if opcion == 1:
        resultado_proceso = texto.upper()
    elif opcion == 2:
        resultado_proceso = texto.lower()
    elif opcion == 3:

        resultado_proceso = texto[0].upper() + texto[1:].lower()
    else:
        resultado_proceso = "Opción no válida"

    return resultado_proceso


print("Escribe el texto que deseas transformar:")
mi_texto = input()

print("\n--- MENÚ DE OPCIONES ---")
print(
    "1. La vida no es esperar a que la tormenta pase, sino aprender a bailar bajo la lluvia"
)
print(
    "2. La vida no es esperar a que la tormenta pase, sino aprender a bailar bajo la lluvia"
)
print(
    "3. La vida no es esperar a que la tormenta pase, sino aprender a bailar bajo la lluvia"
)

print("\nIngresa el número de su elección:")
entrada = input()
mi_opcion = int(entrada)


resultado = transformar_texto(mi_texto, mi_opcion)


print("\nEl resultado es: " + str(resultado))
