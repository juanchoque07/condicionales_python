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
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

print("ingrese 3 temperaturas a registrar")
temp_1 = float(input())
temp_2 = float(input())
temp_3 = float(input())

if temp_1 < temp_2 > temp_3 and temp_1>temp_3:
    print("La maxima de hoy es ", temp_2," °C y la minima sera", temp_3,"°C")
elif temp_1 > temp_2 and temp_2 > temp_3:
    print("La maxima de hoy es ", temp_1, "°C y la minima sera", temp_3,"°C")
elif temp_3 > temp_2 and temp_2 < temp_1:
    print("La maxima de hoy es ", temp_3, "°C y la minima sera", temp_2,"°C")
elif temp_3 > temp_2 and temp_2 > temp_1:
    print("La maxima de hoy es ", temp_3, "°C y la minima sera", temp_1,"°C")
elif temp_1 < temp_2 > temp_3 and temp_1 < temp_3:
    print("La maxima de hoy es ", temp_2," °C y la minima sera", temp_1,"°C")
else:
    print("Pronostico incierto")

#Pronostico incierto nos permite agregar variables a nuestro programa, 
# al saltar por que un caso que no se encuentra comprendido.

temp_promedio = ((temp_1+temp_2+temp_3)/3)

print(" La temperatura promedio para hoy es ",round(temp_promedio,1),"°C")