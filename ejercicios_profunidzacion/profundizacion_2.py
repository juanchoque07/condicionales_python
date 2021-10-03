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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

print("ingrese 3 numeros enteros")
numero_1 = int(input())
numero_2 = int(input())
numero_3 = int(input())

if numero_1 % 2 == 0 and numero_2 % 2 == 0 and numero_3 % 2 == 0:
    print("Todos los numeros ingresados son pares")
elif numero_1 % 2 == 0 and numero_2 % 2 == 0 and numero_3 % 2 != 0:
    print("El tercer numero ingresado es impar y los dos anteriores son pares")
elif numero_1 % 2 == 0 and numero_2 % 2 != 0 and numero_3 % 2 != 0:
    print("Los ultimos dos numeros ingresados son impares y el primero es par")
elif numero_1 % 2 != 0 and numero_2 % 2 == 0 and numero_3 % 2 == 0:
    print("Los ultimos dos numeros ingresados son pares y el primero es impar")
elif numero_1 % 2 != 0 and numero_2 % 2 == 0 and numero_3 % 2 != 0:
    print("El primer y tercer numero ingresado son impares y el segundo es par")
elif numero_1 % 2 != 0 and numero_2 % 2 != 0 and numero_3 % 2 == 0:
    print("Los primeros dos numeros ingresados son impares y el tercero es par")
else:
    print("Todos los numeros ingresados son impares")
