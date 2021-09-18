# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica numérica y cadenas
'''
Enunciado:
Realice un programa que determine cual sería el apellido de una persona
al ingresara los dos nombres completos de sus padres.
En definitiva se solicita crear una variable nueva que reuna
los apellidos.

- Primero el programa debe consultar el nombre completo del padre_1
- Luego el programa debe consultar el nombre completo del padre_2
- Luego debe consultar el nombre del hijo/a
- Debe extraer los apellidos de los padres (ver la nota al final)
- Luego formar el nombre completo del hijo/a utilizando los apellidos
  de sus padres y el nombre ingresado de dicha persona
- Imprimir en pantalla el resultado

NOTA: Para extraer el apellido del nombre completo recomendamos usar
el método "split"
Mostraremos un ejemplo:

direccion_completa = 'Monroe 2716'
calle, altura = direccion_completa.split(' ')

Les dejo por su cuenta a que busquen un poco más acerca de este método
que seguramente utilizarán mucho de acá en adelante.
Les dejamos un link con algunos ejemplos más:
https://www.pythonforbeginners.com/dictionary/python-split

Cualquier duda con el método split pueden consultarla por el campus
'''

print('Jugando con texto')
# Empezar aquí la resolución del ejercicio
print("insert complete name of your father 1")
name_father_1 = str(input())

print ("insert complete name of your father 2")
name_father_2 = str(input())

print ("insert name of your child")
name_child = str(input())

last_name_father_1 = name_father_1.split(" ")
last_name_father_2 = name_father_2.split(" ")
complete_surname_child = last_name_father_1[-1], last_name_father_2[-1]
print ("complete name of the child:", complete_surname_child, name_child)

#prueba
Name_Vater = "Heinz Egon Brecht"
print(Name_Vater)

Name_Mutter = "Rosemarie Friede Zettler"
print(Name_Mutter)

Vorname_Kind = "Heidi"
print(Vorname_Kind)

Nachname_Vater = Name_Vater.split(" ")[-1]
print(Nachname_Vater)
Nachname_Mutter = Name_Mutter.split(" ")[-1]
print(Nachname_Vater)

Kompletter_Name_Kind = Nachname_Vater, Nachname_Mutter, Vorname_Kind
print("Das Kind heisst mit kompletten Namen:", Kompletter_Name_Kind)


