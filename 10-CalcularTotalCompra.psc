Algoritmo CalcularTotalCompra
    // Definir las variables
    Definir precio, cantidad, total Como Real
    
    // Solicitar datos al usuario
    Escribir 'Ingrese el precio del producto (Pan):'
    Leer precio
    
    Escribir 'Ingrese la cantidad comprada de pan:'
    Leer cantidad
    
    // Validar que la cantidad sea válida (mayor a cero)
    Si cantidad <= 0 Entonces
    Escribir 'Error: La cantidad debe ser mayor a cero.'
    Sino
    // Calcular el total
    total <- precio * cantidad
      
      
    Escribir 'El total a pagar por el producto es: $', total
    FinSi
    
FinAlgoritmo