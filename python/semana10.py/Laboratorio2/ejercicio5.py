def procesar_texto(texto, numero):
    if numero not in [1, 2, 3]:
        return "Algo no cuadra en la Matrix"
    else:
        return f"Texto recibido: {texto} | Número válido: {numero}"


texto = input("Escribe un texto: ")
numero = int(input("Escribe un número: "))

print(procesar_texto(texto, numero))
