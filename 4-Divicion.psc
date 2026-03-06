Algoritmo Divicion
	// Solicitar al usuario
	// que ingrese dos números enteros
	// y mostrar la division de ambos.
	Definir NumeroEntrada1, NumeroEntrada2, Total Como real
	Escribir 'Ingrese un numero dividiendo '
	Leer NumeroEntrada1
	Escribir 'Ingrese numero divisor '
	Leer NumeroEntrada2
	//validar que el segundo número no sea cero.
	si NumeroEntrada2 = 0 Entonces Escribir 'Error: No se puede dividir por cero.'
	sino	
		//Esto solo ocurre si el numero No es cero	
		total <- NumeroEntrada1/NumeroEntrada2
	Escribir ' El total de la divison es ', total
	FinSi
FinAlgoritmo
