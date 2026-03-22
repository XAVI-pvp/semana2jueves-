Algoritmo RestarHastaCero
    Definir numero_actual Como Real
    Definir cantidad_a_restar Como Real
    
    Escribir "Ingrese el número inicial:"
    Leer numero_actual
    
    Mientras numero_actual > 0 Hacer
    Escribir "El número actual es: ", numero_actual
    Escribir "Ingrese la cantidad que desea restar:"
    Leer cantidad_a_restar
      
    numero_actual <- numero_actual - cantidad_a_restar
        
    FinMientras
    
    Escribir "El proceso ha finalizado. El número final es: ", numero_actual
FinAlgoritmo