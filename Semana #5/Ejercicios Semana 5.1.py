#Ejemplo #1

"""print("Ejemplo #1")
print("Programa que presenta los pares del 20 al 40 junto a sus cuadrados")

for i in range (20, 41):
    if i % 2 == 0:
        print("Número par: ", i, ", su cuadrado es: ", i**2)"""

#Ejemplo #2

"""print("Ejemplo #2")
print("Programa que presenta el mayor, menor, cantidad de aprobados y reprobados de su clase")

alumnos = input("Ingrese la cantidad de alumnos de su clase: ")
alumnos = int(alumnos)

#Variables
i = 1
mayor = 0
menor = 100
aprobados = 0
reprobados = 0

#Ciclo
while i <= alumnos:
    nota = input("Ingrese la nota del alumno: ")
    nota = int(nota)
    #Saca el mayor
    if (nota >= mayor):
        mayor = nota
    #Saca el menor
    if (nota <= menor):
        menor = nota
    #Saca los aprobados
    if (nota >= 70):
        aprobados += 1
        i += 1
    #Saca los reprobados
    if (nota < 70):
        reprobados += 1
        i += 1

#Impresión de datos
print("La cantidad de aprobados son: ", aprobados)
print("La cantidad de reprobados son: ", reprobados)
print("La nota mayor es: ", mayor)
print("La nota menor es: ", menor)"""
