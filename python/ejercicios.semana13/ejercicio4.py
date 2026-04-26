suma_impares = 0
impares = []
while True:
    num = int(input("Ingresa un número (0 para terminar): "))
    if num == 0:
        break
    if num % 2 != 0:
        suma_impares += num
        impares.append(num)
print("\nSuma de números impares:", suma_impares)
print("Números impares ingresados:")
for n in impares:
    print(n)
