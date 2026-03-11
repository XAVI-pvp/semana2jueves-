Algoritmo Producto_Cociente
	Definir numero1, numero2, producto, cociente Como Real
	
	Escribir "Ingresa el primer número:"
	Leer num1
	Escribir "Ingresa el segundo número:"
	Leer numero2
	
	producto <- numero1 * numero2
	
	Si num2 <> 0 Entonces
		cociente <- numero1 / numero2
		Escribir "Producto: ", producto
		Escribir "Cociente: ", cociente
	Sino
		Escribir "Producto: ", producto
		Escribir "Error: No se puede dividir por cero."
	FinSi
FinAlgoritmo
