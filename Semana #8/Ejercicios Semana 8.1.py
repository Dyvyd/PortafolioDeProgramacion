#Ejercicio #1

print("Programa que convierte un número a binario, octal y hexadecimal")

#Número
num = int(input("Ingrese el número a convertir: "))

#Funciones
def bin(num1):

    binario = []
    
    while num1 != 0:
        modulo = num1 % 2
        cociente = num1 // 2
        binario.insert(0, modulo) #Agrega al vector el número en binario
        num1 = cociente #Añade el resultado de la resta para continuar

    return binario

def oct(num1):

    octal = []
    
    while num1 != 0:
        modulo = num1 % 8
        cociente = num1 // 8
        octal.insert(0, modulo) #Agrega al vector el número en binario
        num1 = cociente #Añade el resultado de la resta para continuar

    return octal

def hex(num1):

    hexa = []
    
    while num1 != 0:
        modulo = num1 % 16

        #Condicional para aplicar las letras
        if(modulo == 10):
            modulo = "A"
        elif(modulo == 11):
            modulo = "B"
        elif(modulo == 12):
            modulo = "C"
        elif(modulo == 13):
            modulo = "D"
        elif(modulo == 14):
            modulo = "E"
        elif(modulo == 15):
            modulo = "F"
            
        cociente = num1 // 16
        hexa.insert(0, modulo) #Agrega al vector el número en binario
        num1 = cociente #Añade el resultado de la resta para continuar

    return hexa

#Invocación de las funciones
resultado_bin = bin(num)
print("El número en binario es: ", resultado_bin)
resultado_oct = oct(num)
print("El número en octal es: ", resultado_oct)
resultado_hex = hex(num)
print("El número en hexadecimal es: ", resultado_hex)
    




