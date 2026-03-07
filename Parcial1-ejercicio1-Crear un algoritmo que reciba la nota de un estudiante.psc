Algoritmo ClasificarNota
    Definir nota Como Real
    
    Escribir "Ingrese la nota del estudiante (0 a 10):"
    Leer nota
    
    Si nota >= 6 Entonces
        Escribir "Estado: APROBADO"
    Sino
        Si nota >= 5 Entonces
            Escribir "Estado: RECUPERACIÓN"
        Sino
            Escribir "Estado: REPROBADO"
        FinSi
    FinSi
    
FinAlgoritmo