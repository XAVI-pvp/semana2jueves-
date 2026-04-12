texto = "Victor Vaquez"
texto_normalizado = texto.casefold()
solo_letras = texto_normalizado.replace(" ", "").isalpha()
print("Texto original:", texto)
print("Texto normalizado:", texto_normalizado)
print("¿Solo contiene letras?:", solo_letras)
