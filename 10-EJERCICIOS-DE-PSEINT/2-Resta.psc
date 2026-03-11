Algoritmo Resta
	//Definimos las variables
	Definir NumeroEntrada1, NumeroEntrada2, Total Como Entero
	//pedimos los datos
	Escribir 'Ingrese el primer numero '
	Leer NumeroEntrada1
	Escribir 'Ingrese un numero a restar '
	Leer NumeroEntrada2
	
	//Realizamos la operacion matematica
	// y que ambos numero sea puedan restar entre  ellos
	si NumeroEntrada2 = 0 Entonces Escribir 'Error: No se puede restar.'	
    sino   
	//Validar que el segundonumero no sea sero
	total <- NumeroEntrada1-NumeroEntrada2
	Escribir ' El total de la resta es ', total
	FinSi
FinAlgoritmo
