correo = input("Por favor, ingresa tu correo electrónico: ")
if "@" in correo:
    print("El correo {} parece válido.".format(correo))
else:
    print("El correo {} no es válido.".format(correo))
