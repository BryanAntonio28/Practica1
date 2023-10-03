# Entrada de datos:
print("Ingresa tu nombre:")
nombre = input()
print(type(nombre))

# Capitalizar y unir palabras:
palabras = nombre.split(" ")
capitalizado = [p.capitalize() for p in palabras]
concatenar = ' '.join(capitalizado)

print("Nombre capitalizado:")
print(concatenar)
