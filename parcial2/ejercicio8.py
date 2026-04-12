texto = """No te deprimas por lo que dejas
atrás,sino agradece por lo que
tuviste la oportunidad de vivir"""
cantidad_a = texto.count("a")
lineas = texto.splitlines()
print("Texto completo:\n", texto)
print("\nCantidad de 'a':", cantidad_a)
print("\nLíneas separadas:")
for linea in lineas:
    print("-", linea)
