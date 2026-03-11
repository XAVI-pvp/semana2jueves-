Algoritmo MostrarPares
    Definir N, i, par Como Entero
    
    Escribir "Ingrese la cantidad de números pares que desea ver:"
    Leer N
    
    Escribir "Los primeros ", N, " números pares son:"
    
    // El bucle va desde 1 hasta N para contar cuántos números mostramos
    Para i <- 1 Hasta N Con Paso 1 Hacer
        par <- i * 2
        Escribir par
    FinPara
    
FinAlgoritmo
