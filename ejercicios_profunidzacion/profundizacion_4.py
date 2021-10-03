# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

from typing import OrderedDict


print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

print("Ingrese 3 palabras")
p_1 = palabra_1 = str(input())
p_2 = palabra_2 = str(input())
p_3 = palabra_3 = str(input())

print(" ¿Como desea ordenar estas palabras?")
ordenado = int(input("ingrese 1 o 2 (alfa ó num)\n"))

#orden alfabetico de mayor a menor

if ordenado == 1:
    print("A seleccionado el orden alfabetico")
    if p_1>p_2>p_3:
        print("El orden es el siguiente {},{},{}".format(p_1,p_2,p_3))
    elif p_1>p_3>p_2:
        print("El orden es el siguiente {},{},{}".format(p_1,p_3,p_2))
    elif p_2>p_1>p_3:
        print("El orden es el siguiente {},{},{}".format(p_2,p_1,p_3))
    elif p_2>p_3>p_1:
        print("El orden es el siguiente {},{},{}".format(p_2,p_3,p_1))
    elif p_3>p_2>p_1:
        print("El orden es el siguiente {},{},{}".format(p_3,p_2,p_1))
    elif p_3>p_1>p_2:
        print("El orden es el siguiente {},{},{}".format(p_3,p_1,p_2))
    elif p_1==p_2==p_3:
        print("mismas palabras")
    elif p_1==p_2>p_3:
        print("mismas palabras ",p_1,"y",p_2,"y antes va",p_3)
    elif p_1==p_2<p_3:
        print("la mayor es ",p_3, "y antes estan", p_2,p_1)
    elif p_1<p_2==p_3:
        print("las palabras ",p_2,"y",p_3,"son iguales y antes va",p_1)
    elif p_1>p_2==p_3:
        print("la mayor es ",p_1,"y le anteceden",p_2,p_3)
    else:
        print("Analizar caso y agregar a programa")
else:
    print("A seleccionado el orden numerico")
    if len(p_1)>len(p_2)>len(p_3):
        print("El orden es el siguiente {},{},{}".format(p_1,p_2,p_3))
    elif len(p_1)>len(p_3)>len(p_2):
        print("El orden es el siguiente {},{},{}".format(p_1,p_3,p_2))
    elif len(p_2)>len(p_1)>len(p_3):
        print("El orden es el siguiente {},{},{}".format(p_2,p_1,p_3))
    elif len(p_2)>len(p_3)>len(p_1):
        print("El orden es el siguiente {},{},{}".format(p_2,p_3,p_1))
    elif len(p_3)>len(p_2)>len(p_1):
        print("El orden es el siguiente {},{},{}".format(p_3,p_2,p_1))
    elif len(p_3)>len(p_1)>len(p_2):
        print("El orden es el siguiente {},{},{}".format(p_3,p_1,p_2))
    elif len(p_1)==len(p_2)==len(p_3):
        print("mismo numero de letras en comun")
    elif len(p_1)==len(p_2)>len(p_3):
        print("la mayor/es es/son ",p_1,"y",p_2,"y le sigue",p_3)
    elif len(p_1)==len(p_2)<len(p_3):
        print("la mayor es ",p_3, "y le siguen", p_2,p_1)
    elif len(p_1)<len(p_2)==len(p_3):
        print("la mayor/es es/son ",p_2,"y",p_3,"y luego va",p_1)
    elif len(p_1)>len(p_2)==len(p_3):
        print("la mayor es ",p_1,"y le siguen",p_2,p_3)
    else:
        print("Analizar caso y agregar a programa")