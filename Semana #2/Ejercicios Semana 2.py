#Ejercicio 1

"""print("Ejercicio #1")

a = input("Ingrese el valor de a: ")
b = input("Ingrese el valor de b: ")
c = input("Ingrese el valor de c: ")
d = input("Ingrese el valor de d: ")

print(d, c, b, a)"""

#Ejercicio 2

"""print("Ejercicio #2")

edad = input("Ingrese el valor de su edad: ")
edad = int(edad) #Lo convierte en entero
suma = edad + 5

print("Dentro de cinco años usted tendrá: " , suma)"""

#Ejercicio 3

"""print("Ejercicio #3")

a = input("Ingrese el valor de a: ")
b = input("Ingrese el valor de b: ")

a = int(a)
b = int(b)
op = (a+b)*2/3

print("La operación (a+b)2/3 da como resultado: " , op)"""

#Ejercicio 4

"""print("Ejercicio #4")

a = input("Ingrese un número: ")
a = int(a)

#Cálculo de potencias
cuadrado = a**2
cubo = a**3

print("El cuadrado del número", a , " es: " , cuadrado)
print("El cubo del número ", a, " es: " , cubo)"""

#Ejercicio 5

"""print("Ejercicio #5")

base = input("Ingrese la base del rectángulo: ")
altura = input("Ingrese la altura del rectángulo: ")

base = int(base)
altura = int(altura)

#Operaciones
area = base * altura
perimetro = base * 2 + altura *2

print("El perímetro del recángulo con los lados ", base , " y " , altura , " es: " , area)
print("El perímetro del recángulo con los lados ", base , " y " , altura , " es: " , perimetro)"""


#Ejercicio 6

"""print("Ejercicio #6")

distancia = input("Ingrese la distancia en kilómetros de la casa a la universidad: ")
kilometros = input("Ingrese el costo del kilómetro: ")
dias = input("Ingrese los días a los que va a la universidad por semana: ")

#variables
distancia = int(distancia)
kilometros = int(kilometros)
dias = int(dias)

#constantes
vueltas = 2
semanas = 15

#Operación
costo_por_cuatri = distancia * kilometros * dias * vueltas * semanas

print("El costo por Cuatrimestre sería de: " , costo_por_cuatri)"""

#Ejercicio 7

"""print("Ejercicio #7")

persona_1 = input("Ingrese la edad de la persona #1: ")
persona_2 = input("Ingrese la edad de la persona #2: ")
persona_3 = input("Ingrese la edad de la persona #3: ")
persona_4 = input("Ingrese la edad de la persona #4: ")
persona_5 = input("Ingrese la edad de la persona #5: ")

persona_1 = int(persona_1)
persona_2 = int(persona_2)
persona_3 = int(persona_3)
persona_4 = int(persona_4)
persona_5 = int(persona_5)

#Operación
promedio = (persona_1 + persona_2 + persona_3 + persona_4 + persona_5)/5

print("El promedio de edades brindadas es: " , promedio)"""


#Ejercicio 8

"""print("Ejercicio #8")

horas = input("Ingrese las horas laboradas: ")
precio = input("Ingrese el precio por hora laborada: ")

#Variables
horas = float(horas)
precio = float(precio)

#constantes
mes = 4.2
deduccion = 10.5
cargas_sociales = 5

#Operaciones
salario_mensual = (horas * precio * mes)
deduccion = deduccion * salario_mensual / 100
cargas_sociales = cargas_sociales * salario_mensual / 100

#Total
salario_mensual = salario_mensual - deduccion - cargas_sociales

print("El salario mensual que usted recibe es: " , salario_mensual)"""

#Ejercicio 9

"""print("Ejercicio #9")

ingresos = input("Inserte los ingresos mensuales: ")
gastos = input("Ingrese los gastos mensuales de alimentación: ")

ingresos = float(ingresos)
gastos = float(gastos)

porcentaje_de_alimentacion = gastos * 100 / ingresos
sobrante = (ingresos - gastos) * 100 / ingresos

print("El gasto en alimentación es de: " , porcentaje_de_alimentacion , "%")
print("El sobrante es de: " , sobrante , "%")"""
