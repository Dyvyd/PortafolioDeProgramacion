#Estudio de caso #2

print("Estudio de caso #2")
print("Programa para agendar citas")

#Variables globales
citas = []
medicos = [["Juan Romero","109858663"],["Sofia Tames","30652745"]]

#Función para el inicio de sesión
def inicio_de_sesion(medicos):
    #Variables locales
    valido = True
    cedula = 0
    op = "indefinido"

    #Ciclo
    while(valido == True):

        #Solicitud de datos
        print("\nInicio de Sesión\n")
        print("Ingrese su cédula")
        cedula = input(">>")

        #Verfica si las credenciales son correctas
        if(cedula == medicos[0][1] or cedula == medicos[1][1]):
            print("\nHa iniciado sesión correctamente\n")
            condicional()
            valido = False
        else:
            #Consulta si gusta salir
            print("Inicio de sesión inválido")
            print("¿Desea Salir?")
            print("1 - Si")
            print("2 - No")
            op = input(">>")

            #Verfica la opción
            if(op == "1"):
                print("Usted saldrá correctamente")
                valido = False
            elif(op == "2"):
                print("Regresará al inicio")
            else:
                print("Ingresó un valor incorrecto, usted saldrá del programa")
                valido = False

#Función del menú principal
def menu():
    print("\nBienvenido al menú")
    print("Ingrese una opción\n")
    print("1 - Ingresar Citas")
    print("2 - Mostrar Citas")
    print("3 - Salir")
    op = input(">>")
    return op

#Función del condicional
def condicional():
    #Variable que determina si la opción es válida
    valido = True

    while(valido == True):
        
        op = menu()
        
        #Condicional
        if(op == "1"):
            ingresar_citas(citas)
        elif(op == "2"):
            mostrar_citas(citas)
        elif(op == "3"):
            print("Usted saldrá correctamente")
            valido = False
        else:
            print("Ingrese una opción válida")

#Función para mostrar las citas
def ingresar_citas(citas):
    # Variables
    fecha = "indefinido"
    hora = "indefinido"
    paciente = "indefinido"
    activado = True

    # Variables para determinar cuando termina el ciclo
    valido = "si"
    sino = True
    valor_correcto = True

    # Ciclo de solicitud de datos del vehículo
    while (valido == "si" or valido == "SI" or valido == "Si"):

        print("Ingrese la fecha de la cita:")
        fecha = input(">>")
        print("Ingrese la hora de la cita:")
        hora = input(">>")
        print("Ingrese el nombre del paciente:")
        paciente = input(">>")

        sino = True
        while(sino == True):
            print("Ingrese si la cita está activa: 1 - Si / 2 - No")
            determinante = input(">>")

            if(determinante == "1"):
                activado = True
                sino = False
            elif(determinante == "2"):
                activado = False
                sino = False
            else:
                print("Ingrese un valor correcto")

        citas.append([fecha,hora,paciente,activado])

        #Determina si se continúa en el ciclo
        print("¿Desea seguir ingresando citas? si/no")
        valido = input(">>")
        if(valido == "no" or valido == "No" or valido == "NO"):
            print("Usted regresará al menú\n")
        elif(valido == "si" or valido == "Si" or valido == "SI"):
            print("Ingrese una nueva cita")
        else:
            print("Ingresó un valor incorrecto")

#Función para mostrar las citas
def mostrar_citas(citas):
    #Variable del estado
    estado = "indefinido"

    #Verifica que no esté vacía la matriz
    if len(citas) == 0:
        print("No hay citas registradas")
    else:
        print("Listado de citas en inventario:")
        for cita in citas:
            print()
            print("Fecha:", cita[0])
            print("Hora:", cita[1])
            print("Paciente:", cita[2])

            #Verfica si la cita está activa
            if(cita[3] == True):
                estado = "Activa"
            elif(cita[3] == False):
                estado = "No activa"
            print(estado)
    


#Invoca la función
inicio_de_sesion(medicos)
    
