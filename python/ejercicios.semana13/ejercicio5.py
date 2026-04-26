clave_correcta = "aguacates"
intentos_fallidos = 0
while True:
    clave = input("Ingresa la contraseña: ")
    if clave == clave_correcta:
        print("Contraseña correcta. Acceso permitido.")
        break
    else:
        print("Contraseña incorrecta.")
        intentos_fallidos += 1
print("\nIntentos fallidos:")
for i in range(intentos_fallidos):
    print("Intento fallido", i + 1)
