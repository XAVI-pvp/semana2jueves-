while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        if edad < 0:
            print("Por favor, ingresa una edad válida.")
        else:
            break
    except:
        print("Error: debes ingresar un número.")
if edad < 18:
    categoria = "Menor de edad"
elif edad < 60:
    categoria = "Mayor de edad"
else:
    categoria = "Adulto mayor"
print("\nResultado:")
print(categoria)
print("\nMostrando mensaje:")
for i in range(1, 4):
    print(f"{i}. Eres: {categoria}")
