texto = "pYTHON"
texto_invertido = texto.swapcase()

texto_final = texto_invertido.ljust(15, "*")
print("Texto original:", texto)
print("Texto invertido:", texto_invertido)
print("Resultado final:", texto_final)
