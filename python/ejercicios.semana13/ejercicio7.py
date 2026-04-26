notas_validas = []
while True:
    nota = float(input("Ingresa una nota (0 a 10) o -1 para terminar: "))
    if nota == -1:
        break
    if 0 <= nota <= 10:
        notas_validas.append(nota)
    else:
        print("Nota inválida, no se toma en cuenta.")
suma = 0
for n in notas_validas:
    suma += n
if len(notas_validas) > 0:
    promedio = suma / len(notas_validas)
    print("\nPromedio:", promedio)
else:
    print("\nNo hay notas válidas para calcular el promedio.")
