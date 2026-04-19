usuario_correcto = "admin"
contrasena_correcta = "1234"
while True:
    usuario = input("Ingresa el usuario: ")
    contrasena = input("Ingresa la contraseña: ")
    for i in range(1):
        if usuario == usuario_correcto and contrasena == contrasena_correcta:
            print("Acceso permitido")

    else:
        print("Acceso denegado")
    opcion = input("¿Deseas intentar nuevamente? (s/n): ")
    while opcion != "s" and opcion != "n":
        opcion = input("Opción inválida. Ingresa s o n: ")
    if opcion == "n":
        print("Programa finalizado")
        break
