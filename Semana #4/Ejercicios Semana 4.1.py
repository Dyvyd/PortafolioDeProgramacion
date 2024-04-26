#Ejercicio #1

"""print("Ejercicio #1")

salario = input("Ingrese su Salario: ")
salario = int(salario)
categoria = input("Ingrese su categoría (1,2,3,4): ")
categoria = int(categoria)

if(categoria == 1):
    salario *= 1.10
else:
    if(categoria == 2):
        salario *= 1.12
    else:
        if(categoria == 3):
            salario *= 1.15
        else:
            if(categoria == 4):
                salario *= 1.20

print("Su salario con aumento es: ", salario)"""

#Ejercicio #2

"""print("Ejercicio #2")

num1 = input("Ingrese el primer número: ")
num1 = int(num1)
num2 = input("Ingrese el segundo número: ")
num2 = int(num2)

if (num1 > num2):
    print("El número mayor es: ", num1)
else:
    if (num2 > num1):
        print("El número mayor es: ", num2)
    else:
        print("Los números son iguales")"""

#Ejercicio #3

"""print("Ejercicio #3")

num1 = input("Ingrese el primer número: ")
num1 = int(num1)
num2 = input("Ingrese el segundo número: ")
num2 = int(num2)
num3 = input("Ingrese el tercer número: ")
num3 = int(num3)

if(num1 > num2 and num1 > num3):
    mayor = num1
else:
    if(num2 > num1 and num2 > num3):
        mayor = num2
    else:
        if(num3 > num1 and num3 > num2):
            mayor = num3

if(num1 < num2 and num1 < num3):
    menor = num1
else:
    if(num2 < num1 and num2 < num3):
        menor = num2
    else:
        if(num3 < num1 and num3 < num2):
            menor = num3

if((num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3)):
    medio = num1
else:
    if((num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3)):
        medio = num2
    else:
        if((num3 > num2 and num3 < num1) or (num3 < num2 and num3 > num1)):
            medio = num3

print("El orden desendente de los números es: ", mayor, medio, menor)"""

#Ejercicio #3

"""print("Ejercicio #3")

anio = input("Ingrese su año de nacimiento: ")
anio = int(anio)

if (anio == 400 or (((anio % 4) == 0) and ((anio % 100)!= 0))):
    print("Su año de nacimiento es bisiesto")
else:
    print("Su año de nacimiento no es bisiesto")"""
