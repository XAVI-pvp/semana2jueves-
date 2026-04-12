archivo = "VICTOR.txt"
texto = archivo.replace(".txt", "")
texto = texto.replace("ING. ", "")
texto_final = texto.lower()
print("Archivo original:", archivo)
print("Sin extensión:", texto)
print("Resultado final:", texto_final)
