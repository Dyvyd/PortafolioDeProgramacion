#Ejercicio #1

"""print("Ejercicio #1")
print("Programa que muestra los kilómetros recorridos en la semana")

#Variables
resultados = []
dia = ["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]

#Acumula los datos
for i in range(7):
    print("Ingrese los kilómetros del", dia[i])
    km = input(">>")
    resultados.append(km)

#Presenta los resultados
print("\n Los resultados son: \n")
for i in range(7):
    print("El día", dia[i], "usted hizo: ", resultados[i], "km")"""

#Ejercicio #2

"""print("Ejercicio #2")
print("Programa que muestra los nombres de las reservas de cada butaca")

#Variable
butacas = []

#Acumulación de datos
for i in range(10):
    print("Ingrese el nombre de la persona que ocupará la butaca #", i + 1)
    nombre = input(">>")
    butacas.append(nombre)

#Presenta los resultados
print("\n Los resultados son: \n")
for i in range(10):
    print("La persona que reservó la butaca #", i + 1, "es", butacas[i])"""

#Ejercicio #3

"""print("Ejercicio #3")
print("Programa que imprime una palabra al revés")

#Variables
reves = []

#Inserción de datos
print("Ingrese una palabra que desee invertir: ")
palabra = input(">>")

#Obtiene el largo de la palabra
largo = len(palabra)
determinante = largo - 1 #Determina la letra que se va a colocar al vector

#Recorre la palabra
for i in range(largo):
    reves.append(palabra[determinante])
    determinante -= 1 #Disminuye en cada vuelta

#Ordena el vector
ordenado = ""
for i in range (largo):
 ordenado += reves[i]

print("La palabra invertida es", ordenado)"""

#Ejercicio #4

print("Ejercicio #3")
print("Programa que presenta el monto ganado por semana")

#Variables
monto = []
dia = ["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]
total = 0
menor = 9999999999999

#Acumula los datos
for i in range(7):
    print("Ingrese el dinero recaudado el", dia[i])
    dinero = int(input(">>"))
    monto.append(dinero)
    total += dinero
    #Determina si es menor
    if(dinero <= menor):
        menor = dinero

#Presenta los resultados
print("\n Los resultados son: \n")
for i in range(7):
    print("El día", dia[i], ", usted recaudó: ", monto[i])

print("El monto menor que recaudo es: ", menor)
print("El total recaudado por la semana es: ", total)
