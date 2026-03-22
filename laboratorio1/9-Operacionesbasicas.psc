Algoritmo sumarestamultiplicaciondivision
	
	// Solicitar al usuario
	// que ingrese dos números enteros
	// y mostrar la suma,resata, multiplicacion y division  de ambos.
	Definir NumeroEntrada1, NumeroEntrada2, numeroTotal Como Entero
	Escribir 'Ingrese un numero para suma,resata, multiplicacion y division'
	Leer NumeroEntrada1
	Escribir 'Ingrese un numero para sumar,resata, multiplicacion y division  '
	Leer NumeroEntrada2
	
	si NumeroEntrada1> 0 y NumeroEntrada2> 0 
	numerototal <- NumeroEntrada1+NumeroEntrada2
	Escribir ' El numeroTotal de la suma es ', numeroTotal
FinSi
	si NumeroEntrada2 = 0 Entonces Escribir 'Error: No se puede restar.'	
	sino 
	//Validar que el segundonumero no sea sero
	total <- NumeroEntrada1-NumeroEntrada2
	Escribir ' El numeroTotal de la resta es ', total
FinSi
    // Simplemente asigna el valor y muéstralo
    numeroTotal <- NumeroEntrada1 * NumeroEntrada2
    Escribir ' El total de la multiplicacion es ', numeroTotal
    si NumeroEntrada2 = 0 Entonces Escribir 'Error: No se puede dividir por cero.'
	sino	
	//Esto solo ocurre si el numero No es cero	
	total <- NumeroEntrada1/NumeroEntrada2
	Escribir ' El numeroTotal de la divison es ', total
FinSi
FinAlgoritmo
