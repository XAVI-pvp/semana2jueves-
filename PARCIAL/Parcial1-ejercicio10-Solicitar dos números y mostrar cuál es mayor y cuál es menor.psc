Algoritmo Comparar_Numeros
	Definir numero1, numero2 Como Real
	
	Escribir "Ingresa el primer número:"
	Leer numero1
	Escribir "Ingresa el segundo número:"
	Leer numero2
	
	Si numero1 > numero2 Entonces
		Escribir "El mayor es: ", num1
		Escribir "El menor es: ", num2
	Sino
		Si numero1 < numero2 Entonces
			Escribir "El mayor es: ", numero2
			Escribir "El menor es: ", numero1
		Sino
			Escribir "Ambos números son iguales."
		FinSi
	FinSi
FinAlgoritmo
