suma = 0
numeros_validos = []
while suma <= 100:
    num = int(input("Ingresa un número: "))
    if num < 0:
        print("Número negativo ignorado.")
        continue
    suma += num
    numeros_validos.append(num)
    print("Suma actual:", suma)
print("\nNúmeros válidos ingresados:")
for n in numeros_validos:
    print(n)

print("Suma final:", suma)
