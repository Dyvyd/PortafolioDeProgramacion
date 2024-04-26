"""#Ejemplo #1

print("Ejemplo #1")
print("Programa que presenta el promedio de vueltas de Formula 1")

#Variables
tiempo = 0
pits = 0
porcentaje_de_vuelta = 1

for i in range (10):
    if i <= 10 :

        #Vueltas
        print("Digite el tiempo que recorrió en la vuelta #", i + 1)
        vuelta = input(">>")
        tiempo += int(vuelta)#Acumulador de tiempo

        #Pits
        print("Digite el tiempo que utilizó en los PITS de la vuelta #", i + 1)
        pit = input(">>")
        pits += int(pit)#Acumulador de pits

        #Porcentaje
        porcentaje_de_vuelta = int(pit) * 100 / int(vuelta)
        print("El porcentaje de PITS de la vuelta ", i + 1, " es: ", porcentaje_de_vuelta)

#Operaciones
promedio_de_vuelta = tiempo / 10
promedio_de_pits = pits / 10

print("El promedio de vueltas es: ", promedio_de_vuelta)
print("El promedio de PITS es: ", promedio_de_pits)"""



"""#Ejemplo #2

print("Ejemplo #2")
print("Programa que analiza la estatura de los niños")

num = input("Digite la cantidad de niños: ")
num = int(num)

#Variables
contador = 0
contador_de_menos_de_100 = 0
contador_de_menos_de_120 = 0
contador_de_menos_de_130 = 0
contador_de_menos_de_140 = 0
contador_de_mas_de_140 = 0
promedio = 0

#Ciclo
for i in range (num):
    if i <= num :
        print("Digite la estatura del niño #", i + 1)
        estatura = int(input(">>"))
        if (estatura < 100):
            contador_de_menos_de_100 += 1
        elif (estatura <= 120):
            contador_de_menos_de_120 += 1
        elif (estatura <= 130):
            contador_de_menos_de_130 += 1
        elif (estatura <= 140):
            contador_de_menos_de_140 += 1
        else:
            contador_de_mas_de_140 += 1
        contador += 1
        promedio += estatura

#Resultados
promedio /= num

print("La cantidad de niños de menos de 100 cm es: ", contador_de_menos_de_100)
print("La cantidad de niños de entre 100 cm y 120 cm es: ", contador_de_menos_de_120)
print("La cantidad de niños de entre 121 cm y 130 cm es:", contador_de_menos_de_130)
print("La cantidad de niños de entre 131 cm y 140 cm es: ", contador_de_menos_de_140)
print("La cantidad de niños de más de 140 cm es: ", contador_de_mas_de_140)
print("El promedio de estatura es: ", promedio)"""



"""#Ejemplo #3

print("Ejemplo #3")
print("Programa que muestra los primeros 10 números divisibles de un número")


num = input("Digite el numero: ")
num = int(num)

#Variables
lista = []
contador = 1


#Ciclo
i = 0
while i < 10:
    if (num % contador == 0):
        i += 1
        lista.append(contador)
    contador += 1
        
print("Los números que son divisibles entre: ", num, " son: ", lista)"""

#Ejemplo #4

print("Ejemplo #4")
print("Programa que indica cuanto dinero se necesita para que 15 personas ganen 500$")

#Variables
acumulador = 0

#Ciclo
for i in range (15):
    if i < 15 :
        print("Ingrese el salario del trabajor #", i + 1)
        salario = input(">>")
        if int(salario) < 500:
            acumulador += 500 - int(salario)

#Resultado
print("La cantidad necesaria para que todos los trabajadores ganen 500$ es de: ", acumulador)
