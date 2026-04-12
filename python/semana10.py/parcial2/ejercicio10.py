texto = "Python2026"
es_alfanumerico = texto.isalnum()
if es_alfanumerico:
    texto_minuscula = texto.lower()
    texto_final = texto_minuscula.replace("2026", "")
else:
    texto_final = "El texto no es alfanumérico"
print("Texto original:", texto)
print("¿Es alfanumérico?:", es_alfanumerico)
print("Resultado final:", texto_final)
