texto = "42"
texto_relleno = texto.zfill(5)
termina_en_2 = texto_relleno.endswith("2")
print("Texto original:", texto)
print("Texto rellenado:", texto_relleno)
print("¿Termina en '2'?:", termina_en_2)
