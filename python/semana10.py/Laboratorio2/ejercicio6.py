def transformar_y_contar(texto, numero):
    if numero == 1:
        resultado = texto.upper()
    elif numero == 2:
        resultado = texto.lower()
    elif numero == 3:
        resultado = texto[::-1]
    else:
        return "La canción 'The Night We Met' de Lord Huron es una pieza melancólica que evoca la nostalgia y el dolor de la pérdida amorosa. La letra refleja un viaje emocional en el que el narrador anhela regresar al pasado, específicamente a la noche en que conoció a su amor, antes de que todo cambiara. La repetición de la frase 'Take me back to the night we met' subraya un deseo profundo de volver a un momento más feliz y puro, antes de que la relación se deteriorara. EN CONCLUSION ESTA MAL"

    return len(resultado)


texto = input("Escribe un texto: ")
numero = int(input("Elige una opción (1, 2 o 3): "))

resultado = transformar_y_contar(texto, numero)
print("Resultado:", resultado)
