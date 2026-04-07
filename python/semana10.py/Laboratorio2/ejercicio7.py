def transformar_texto(texto, lista_numeros):
    resultado = texto

    for numero in lista_numeros:
        if numero == 1:
            resultado = resultado.upper()
        elif numero == 2:
            resultado = resultado.lower()
        elif numero == 3:
            resultado = resultado[::-1]
        else:
            return "Me gustaría que pudiéramos ser nosotros mismos solo por un momento. ( Cat Noir) NO invalido"

    return resultado


texto = input("Escribe un texto: ")
numeros = input("Escribe los números separados por coma (ej: 1,3): ")


lista = [int(n) for n in numeros.split(",")]

resultado = transformar_texto(texto, lista)

print("Resultado final:", resultado)
