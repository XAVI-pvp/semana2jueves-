Algoritmo  Sumar3numeros 
	
	Definir NumeroEntrada1, NumeroEntrada2, NumeroEntrada3, numeroTotal Como Entero
	Escribir 'Ingrese un numero para sumar '
	Leer NumeroEntrada1
	Escribir 'Ingrese un numero para sumar '
	Leer NumeroEntrada2
	Escribir 'Ingrese un numero para sumar '
	Leer NumeroEntrada3
	//lRealizamo la operacion directamente
	si NumeroEntrada1> 0 y NumeroEntrada2> 0 y NumeroEntrada3> 0 
		numerototal <- NumeroEntrada1+NumeroEntrada2+NumeroEntrada3
		Escribir ' El total de la suma es ', numeroTotal
	sino
		Escribir 'Error: Los Numeros deben ser mayores a cero.'
	FinSi
FinAlgoritmo	
