positivos = 0
negativos = 0
num = int(input("Ingresa un número (0 para terminar): "))
while num != 0:
    # IF para clasificar
    if num > 0:
        positivos += 1
    else:
        negativos += 1
    num = int(input("Ingresa otro número (0 para terminar): "))
# FOR para mostrar resumen
print("\nResumen de resultados:")
datos = [positivos, negativos]
nombres = ["Positivos", "Negativos"]
for i in range(2):
    print(nombres[i] + ":", datos[i])
