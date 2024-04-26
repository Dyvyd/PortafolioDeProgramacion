#Ejercicio #1

#Biblioteca para gestionar archivos
import os

print("Ejercicio #1")
print("Programa que muestra guarda las notas de los estudiantes de Programación básica")

#Función del menú principal
def menu():
    print("\nMenú principal")
    print("Ingrese la opción que guste")
    print("1 - Visualizar notas")
    print("2 - Agregar notas")
    print("3 - Salir")
    op = input(">>")
    return op

#Función para gestionar las opciones
def condicional():
    #Variable que indica si se sigue en el ciclo
    valido = "si"
    #Ciclo para revisar la opción del menú
    while(valido == "si"):
        
        #invoca el menu
        op = menu()
        
        if(op == "1"):
            mostrar_notas()
        elif(op == "2"):
            ingresar_notas()
        elif(op == "3"):
            print("Usted saldrá correctamente")
            valido = "no"
        else:
            print("Ingrese una opción válida")

def ingresar_notas():
    #Variable que indica si se sigue en el ciclo
    valido = "si"
    respuesta = "si"
    #Ciclo para seguir agregando
    while(valido == "si"):

        #Variables iniciales
        nombre = "indefinido"
        grupo = 0
        calificación = 0

        #Solicitud de datos
        print("Ingrese el nombre del estudiante:")
        nombre = input(">>")
        print("Ingrese el grupo del estudiante:")
        grupo = input(">>")
        print("Ingrese la nota del estudiante:")
        nota = input(">>")

        #Abre el archivo
        file = open("notas.txt","a")
        #Inserción de datos
        file.write("Nombre = ")
        file.write(nombre)
        file.write(", Grupo = ")
        file.write(grupo)
        file.write(", Nota = ")
        file.write(nota)
        file.write("\n")
        #Cierra el archivo
        file.close()

        determinante = True
        while(determinante == True):
            #Consulta si desea continuar
            print("¿Desea seguir ingresando notas?")
            respuesta = input(">>")
            
            #Condicional que revisa la respuesta
            if(respuesta == "si" or respuesta == "Si" or respuesta == "SI"):
                valido = "si"
                determinante = False
            elif(respuesta == "no" or respuesta == "No" or respuesta == "NO"):
                print("Usted saldrá correctamente")
                valido = "no"
                determinante = False
            else:
                print("Ingrese un valor válido")

def mostrar_notas():
    print("Las notas almacenadas son: \n")

    #Abre el archivo
    file = open("notas.txt","r")
    #Variable que almacena el mensaje
    mensaje = file.read()
    print(mensaje)
    #Cierra el archivo
    file.close()

#Invoca la función condicional
condicional()

