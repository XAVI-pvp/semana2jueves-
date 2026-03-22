frase = input("Escribe una frase: ")
empieza_con_hola = frase.startswith("Hola")
if empieza_con_hola:
    print("Acceso concedido al club de los saludos.")
else:
    print("Error: No dijiste la palabra mágica.")
