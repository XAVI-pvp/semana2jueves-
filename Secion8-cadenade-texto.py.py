# las comillas triples son las que se encargan de hacer
# Cadenas de texto largas sin mdoficar el formato.
# texto corto
Cancion = " la noche, la que te conocí ''' o " ""


# textos largos ''' o """
Cancion = """No soy el único viajero
Que se perdió tratando de fingir
Buscando un camino para encontrarte
Y volver a esa noche cuando te vi

Y así podré gritarme
¿Qué chingados se supone que debo hacer?
Y así podré gritarme
Que no debo aferrarme a ti, bendita mujer

Tuve todo y me quedé solo sin ti
Llévame a la noche, la que te conocí
Todavía está el fantasma que quedó después de ti
Llévame a la noche, la que te conocí

Y devuélveme a esa noche
En la que te conocí, chiquita
Y así suena su compa Marquitos

Esas noches, cuando tenías miedo
Extraño hacerte sonreír
Cuando fantaseaba por un beso
Quiero volver a la noche en que te conocí

Tuve todo y me quedé solo sin ti
Llévame a la noche, la que te conocí
Todavía está el fantasma que quedó después de ti
Llévame a la noche, la que te conocí

Llévame a la noche, la que te conocí. """

##print(cancion)

## computadora -> que variable queres imprimir
## print()
## computadora -> que variable quieres imprimir
## print() =>
# void -> no devuelve nada
# objetivo -> devuelve un tipo de dato

## realizar una wiki tambien puede darkle doble  clic al documento
## y se les desplegara el editor de texto

## MAYUSCULAS
## Mutabilidad -> siempre debemos evitar transformar el objeto inicial
## Clases -> Estereotipo (como un molde)
## Propiedades ->
## color
## tipo de motor (electrico o gasolina)
## ojos
## color de pelo
# funciones -> string ( cadenas de texto) es un objeto
# moverse
# frenar
# cargarse
# descargarse

# Cancion es un espacio de memoria  para string
# se va a llenar con el contenido de  Canacion alterar con la accion Upper ( mayusculas)
Cancion_Mayusculas = Cancion.upper()
##print(Cancion_Mayusculas)

# convertir en minusculas
## string .lower

Cancion_minuscula = Cancion.lower()
print(Cancion_minuscula)

## tiene que ingresar 100 nombres en mayuscula
mensaje = "hOlA kACe progRMando o qUe HaCe"
## Capitalize a que la primera letra de cada palabra sea mayuscula
mensajeCorrecto = mensaje.capitalize()
print(mensajeCorrecto)

## Las flipantes aventuras de ladybug
titulo = "Las flipantes aventuras de ladybug"
titulocorrecto = titulo.title()
print(titulocorrecto)

## swapCase() permite cambiar entre mayuscula y minuscula
swapCasetitulo = titulocorrecto.swapcase()
print(swapCasetitulo)
nombre= "Victor"
nombre2= "Javier"
Comparar = nombre.casefold() == nombre2.casefold()
print(Comparar)

## metodos de validacion
# false numeros o espacio
# true tiene solo letras
numeros = "512"
solo_letras = "La carrera me esta consumiendo "
coro = "todo por ese titulo"

quieroSoloLetras = solo_letras.isalpha()
print(quieroSoloLetras)
