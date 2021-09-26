# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

print("Ejercicio de práctica numérica")

# Comparadores
# Ingrese dos números cualesquiera y realice las siguientes
# comparaciones entre ellos

numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda

if numero_1 > numero_2:
    print("{} es mayor que {}".format(numero_1,numero_2))
else:
    print("{} es menor que {}".format(numero_1,numero_2))    

# *** Verifique si el numero_1 positivo, negativo o cero
# *** Imprima el resultado en cada caso
# *** Verifique si el numero_1 es mayor a 0 y menor a 100
# *** Imprima en pantalla si se cumple o no la condición

# Ejercicio mezclado 2 en 1***

if numero_1 < 0:
    print("El numero ingresado es negativo")
elif (numero_1 > 0 and numero_1 < 100):
    print("el numero es positivo y menor que 100 y cumple con la condicion")
elif numero_1 == 0:
    print("el numero ingresado es cero")
else:
    print("El numero es positivo pero no es menor a 100")

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición

if (numero_1 < 10 or numero_2 > -2):
    print("Cumple con la condicion de ser menor a 10 ó mayor que -2")
else:
    print("No cumple con la condicion de ser menor a 10 ó mayor que -2")

print("Ejercicio Terminado!")