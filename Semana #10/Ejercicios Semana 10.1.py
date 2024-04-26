#Ejercicio #1

#Biblioteca para generar aleatoriamente
import random

print("Ejercicio #1")
print("Programa que muestra donde se encuentra la letra de la matriz")

#Matriz
aleatorio = [[0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0]]

#Genera el lugar donde se pondrá la letra
fila_aleatoria = random.randint(0,4)
columna_aleatoria = random.randint(0,4)

#Coloca la letra en el lugar aleatorio
aleatorio[fila_aleatoria][columna_aleatoria] = "L"

#Ciclo para recorrer la matriz
for fila in range(5):
    for columna in range(5):
        #Verfica si ahí está la letra
        if(aleatorio[fila][columna] == "L"):
            print("El lugar en donde se encuentra la letra es en la fila", fila + 1, "y en la columna", columna + 1)
            
#Imprime la matriz
print(aleatorio)

#Ejercicio #2

"""print("Ejercicio #2")
print("Programa que muestra la nota final de sus estudiantes")

#Matriz
estudiantes = [[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]]

#Ciclo que solicita las notas
def agregar(matriz):
    for fila in range(5):
        for columna in range(4):
            nota = 0
            print("Ingrese la nota del estudiante #:", fila + 1, "En la actividad #:", columna + 1)
            nota = int(input(">>"))
            estudiantes[fila][columna] = nota #Agrega la nota a la matriz

#Cálculo e impresión del resultado
def consulta(matriz):
    print("Ingrese el estudiante al que desea consultar")
    estudiante = int(input(">>"))

    #Calculo del total
    total = matriz[estudiante - 1][0] + matriz[estudiante - 1][1] + matriz[estudiante - 1][2] + matriz[estudiante - 1][3]

    print("El total del estudiante es: ", total)

def menu():
    #Variables
    salir = "no"
    ha_pasado = False #Determina si se agregaron datos en la matriz

    while(salir == "no"):

        #Opciones de menu
        print("Menú")
        print("1 - Agregar ")
        print("2 - Consultar ")
        print("3 - Salir")
        print("Ingrese la opción que desea ingresar: ")
        op = input(">>")

        #Condicional del menú
        if(op == "1"):
            ha_pasado = True
            agregar(estudiantes)
        elif(op == "2"):
            if(ha_pasado == False):
                print("No se han agregado estudiantes")
            else:
                consulta(estudiantes)
        elif(op == "3"):
            print("Usted saldrá correctamente")
            salir = "si"
        else:
            print("Usted ha seleccionado una opción incorrecta")

#Invoca el menú
menu()"""


#Ejercicio #3

"""print("Ejercicio #3")
print("Programa que reserva espacios en la microbus")

#Matriz
reservas = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

salir = "no"
while(salir == "no"):
    #Muestra los horarios
    print("Ingrese el horario que desea reservar:")
    print("1 - 7:00 am")
    print("2 - 11:00 am")
    print("3 - 2:00 9m")
    print("4 - 4:00 pm")
    print("5 - Salir del programa")
    horario = int(input(">>"))

    #Verifica que el horario sea válido
    if(horario >= 1 and horario <= 4):
        print("Ingrese el lugar que desea reservar: (1-20)")
        espacio = int(input(">>"))

        if(reservas[horario - 1][espacio - 1] == 1):
            print("Este espacio ya se ha reservado")
        elif(espacio >= 1 and horario <= 20):
            reservas[horario - 1][espacio - 1] = 1
            print(f"Se ha reservado en correctamente en el horario: {horario} Con el espacio: {espacio}")
        else:
            print("Usted ha ingresado un valor inválido")

    elif(horario == 5):
        print("Vuelva pronto")
        salir = "si"
    else:
        print("Ingrese un valor válido")"""




    

