frase = input("Escribe una frase: ")
termina_con_punto = frase.endswith(".")
if termina_con_punto:
 print("La frase '{}' está bien puntuada con su punto final.".format(frase))
else:
 print("A la frase '{}' le hace falta el punto final.".format(frase))