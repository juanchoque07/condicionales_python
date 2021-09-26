# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print("La primera palabra es mayor alfabeticamente que la segunda")
else:
    print("La primera palabra es menor alfabeticamente que la segunda")

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
cant_letras_1 = len(texto_1)
cant_letras_2 = len(texto_2)

if cant_letras_1 < cant_letras_2:
    print("La segunda palabra tiene mas letras que la primera")
elif cant_letras_1 == cant_letras_2:
    print("Tienen igual cantidad de letras ambas palabras")
else:
    print("La primera palabra tiene mas letras que la segunda")

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

letra_texto_1 = texto_1[0]
letra_texto_2 = texto_2[0]

if letra_texto_1 > letra_texto_2:
    print("La primera letra del texto_1 es mayor en valor que la primer letra del texto_2")
elif letra_texto_1 == letra_texto_2:
    print("Tienen el mismo valor ambas primeras letras")
else:
    print("La primera letra del texto_2 es mayor en valor que la primer letra del texto_1")

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if copia_texto_1 == texto_1:
    print("{} es igual que {}".format(copia_texto_1,texto_1))
elif copia_texto_1 != texto_2:
    print("{} es distinta que {}".format(copia_texto_1,texto_2))
else:
    print("{} es igual que {} o distinto a {}".format(copia_texto_1,texto_2,texto_1))

print("Ejercicio Terminado!")