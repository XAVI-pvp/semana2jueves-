import random

numero_secreto = random.randint(1, 100)
intentos = []
print("Adivina el número (entre 1 y 100)")
while True:
    intento = int(input("Ingresa tu número: "))
    intentos.append(intento)
    if intento < numero_secreto:
        print("El número es mayor.")
    elif intento > numero_secreto:
        print("El número es menor.")
    else:
        print("¡Correcto! Adivinaste el número.")
        break
print("\nIntentos realizados:")
for i in intentos:
    print(i)
