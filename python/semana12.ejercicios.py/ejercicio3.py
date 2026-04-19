while True:
    try:
        nota = int(input("Ingresa una nota (0-10): "))
        if 0 <= nota <= 10:
            break
        else:
            print("La nota debe estar entre 0 y 10.")
    except:
        print("Error: ingresa un número válido.")
if nota >= 9:
    resultado = "Excelente"
elif nota >= 7:
    resultado = "Bueno"
elif nota == 6:
    resultado = "Aprobado"
else:
    resultado = "Reprobado"

print("\nResultado:")
print(resultado)
