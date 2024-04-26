#Ejercicio #1

def sumar(num1,num2):
    resultado = num1 + num2
    return resultado

def resta(num1,num2):
    resultado = num1 - num2
    print("La resta es: ", resultado)
    return resultado

def multi(num1,num2):
    resultado = num1 * num2
    print("La multiplicación es: ", resultado)
    return resultado

def dividir(num1,num2):
    resultado = num1 / num2
    print("La division es: ", resultado)
    return resultado



print("Bienvenido a la calculadora")

#Números
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el primer número: "))

operacion = input("Ingrese la operación que desea: a)Suma b)Resta c)Multiplicación d)División: ")

resultado_de_operación = None

if(operacion == "a"):
    resultado_de_operación = sumar(a,b)
elif(operacion == "b"):
    resultado_de_operación = resta(a,b)
elif(operacion == "c"):
    resultado_de_operación = multi(a,b)
elif(operacion == "d"):
    resultado_de_operación = dividir(a,b)
else:
    print("Ingresó una opción inválida")

if (resultado_de_operación != None):
    print("El resultado es: ", resultado_de_operación)




