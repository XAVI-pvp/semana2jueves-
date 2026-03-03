Algoritmo RestarHastaCero
	Definir numero_actual Como Real
	Definir cantidad_a_restar Como Real
	Definir proceso_terminado Como Logico
	
	proceso_terminado <- Falso
	
	Escribir "Ingrese el número inicial:"
	Leer numero_actual
	
	Repetir
		Escribir "El número actual es: ", numero_actual
		Escribir "Ingrese la cantidad que desea restar:"
		Leer cantidad_a_restar
		
		numero_actual <- numero_actual - cantidad_a_restar
		
		Si numero_actual <= 0 O NO (numero_actual > 0) Entonces
			proceso_terminado <- Verdadero
		FinSi
		
	Hasta Que proceso_terminado = Verdadero
	
	Escribir "El proceso ha finalizado. El número es: ", numero_actual
FinAlgoritmo
