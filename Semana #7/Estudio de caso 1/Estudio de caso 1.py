#Estudio de caso #1

print("Estudio de Caso #1")
print("Programa que presenta los ganadores de la rifa por semana")

#Variables
ganador_semana1 = 0
ganador_semana2 = 0
ganador_semana3 = 0
ganador_semana4 = 0

paso_ganadores = False

#Define el menú principal
def menu():
    print("Menú Principal")
    print("Seleccione la opción a ingresar")
    print("[1] Definición de números")
    print("[2] Participar en semana #1")
    print("[3] Participar en semana #2")
    print("[4] Participar en semana #3")
    print("[5] Participar en semana #4")
    print("[6] Salir")
    op = int(input(">>"))
    return op

#Determina la opción del menú
def condicional():
    
    op = menu()
    if op == 1:

        #Variables de ganadores
        global ganador_semana1
        ganador_semana1 = 0
        global ganador_semana2
        ganador_semana2 = 0
        global ganador_semana3
        ganador_semana3= 0
        global ganador_semana4
        ganador_semana4 = 0
        global paso_ganadores
        paso_ganadores = True

        #Determinan si el número es válido
        numero_valido1 = False 
        numero_valido2 = False
        numero_valido3 = False
        numero_valido4 = False

        #Solicitud de los ganadores

        #Ciclo que determina el número ganador
        while (numero_valido1 == False):
            print("Ingrese el número ganador de la semana #1")
            ganador_semana1 = input(">>")
            ganador_semana1 = int(ganador_semana1)
            if(ganador_semana1 <= 100 and ganador_semana1 >= 1):
                numero_valido1 = True
            else:
                print("Ingrese un número válido")

        while (numero_valido2 == False):
            print("Ingrese el número ganador de la semana #2")
            ganador_semana2 = input(">>")
            ganador_semana2 = int(ganador_semana2)
            if(ganador_semana2 <= 100 and ganador_semana2 >= 1):
                numero_valido2 = True
            else:
                print("Ingrese un número válido")
        
        while (numero_valido3 == False):
            print("Ingrese el número ganador de la semana #3")
            ganador_semana3 = input(">>")
            ganador_semana3 = int(ganador_semana3)
            if(ganador_semana3 <= 100 and ganador_semana3 >= 1):
                numero_valido3 = True
            else:
                print("Ingrese un número válido")
        
        while (numero_valido4 == False):
            print("Ingrese el número ganador de la semana #4")
            ganador_semana4 = input(">>")
            ganador_semana4 = int(ganador_semana4)
            if(ganador_semana4 <= 100 and ganador_semana4 >= 1):
                numero_valido4 = True
            else:
                print("Ingrese un número válido")

        print("Ha ingresado correctamente los ganadores")
        condicional()
        
    elif op == 2:
        print("Semana #1")

        #Verifica si ya se han ingresado ganadores
        if (paso_ganadores == True):
            #Variables para los resultados de la semana
            i = 1
            total = 0
            nombre_ganador = "indefinido"
            cedula_ganador = 0
            monto_ganador = 0

            #Ciclo que recorre los cien participantes
            while(i <= 100):
                #Solicitud de variables locales
                print("Participante #", i)
                print("Ingrese su nombre: ")
                nombre = input(">>")
                print("Ingrese su Cédula:")
                cedula = input(">>")
                cedula = int(cedula)
                print("Ingrese el monto a aportar: 500/1000/2000/5000")
                monto = input(">>")
                monto = int(monto)

                if(monto == 500 or monto == 1000 or monto == 2000 or monto == 5000):
                    if (i == ganador_semana1):
                        nombre_ganador = nombre
                        cedula_ganador = cedula
                        monto_ganador = monto
                    i += 1
                    total += monto
                else:
                    print("Ingrese valores correctos")

            #Impresión de resultados de la semana
            print("El ganador de la semana #1 es:")
            print("Nombre: ", nombre_ganador)
            print("Cédula: ", cedula_ganador)
            #Determina el premio
            if(monto_ganador == 500):
                print("Usted se ha ganado una hamburguesa con papas y gaseosa")
            if(monto_ganador == 1000):
                print("Usted se ha ganado un cupon de cena para 2 personas")
            if(monto_ganador == 2000):
                print("Usted se ha ganado un día en el parque de diversiones con transporte y comida pago para 3 personas")
            if(monto_ganador == 5000):
                print("Usted se ha ganado un fin de semana todo incluido en hotel paradisiaco para 2 personas")
            #Imprime el total de la semana
            print("Total de la semana #1: ", total)
            
        else:
            print("No se han ingresado ganadores")
            condicional()
            
    elif op == 3:
        print("Semana #2")

        #Verifica si ya se han ingresado ganadores
        if (paso_ganadores == True):

            #Variables para los resultados de la semana
            i = 1
            total = 0
            nombre_ganador = "indefinido"
            cedula_ganador = 0
            monto_ganador = 0

            #Ciclo que recorre los cien participantes
            while(i <= 100):
                #Solicitud de variables locales
                print("Participante #", i)
                print("Ingrese su nombre: ")
                nombre = input(">>")
                print("Ingrese su Cédula:")
                cedula = input(">>")
                cedula = int(cedula)
                print("Ingrese el monto a aportar: 500/1000/2000/5000")
                monto = input(">>")
                monto = int(monto)

                if(monto == 500 or monto == 1000 or monto == 2000 or monto == 5000):
                    if (i == ganador_semana2):
                        nombre_ganador = nombre
                        cedula_ganador = cedula
                        monto_ganador = monto
                    i += 1
                    total += monto
                else:
                    print("Ingrese valores correctos")

            #Impresión de resultados de la semana
            print("El ganador de la semana #2 es:")
            print("Nombre: ", nombre_ganador)
            print("Cédula: ", cedula_ganador)
            #Determina el premio
            if(monto_ganador == 500):
                print("Usted se ha ganado una hamburguesa con papas y gaseosa")
            if(monto_ganador == 1000):
                print("Usted se ha ganado un cupon de cena para 2 personas")
            if(monto_ganador == 2000):
                print("Usted se ha ganado un día en el parque de diversiones con transporte y comida pago para 3 personas")
            if(monto_ganador == 5000):
                print("Usted se ha ganado un fin de semana todo incluido en hotel paradisiaco para 2 personas")
            #Imprime el total de la semana
            print("Total de la semana #2: ", total)
            
        else:
            print("No se han ingresado ganadores")
            condicional()
            
    elif op == 4:
        print("Semana #3")

        #Verifica si ya se han ingresado ganadores
        if (paso_ganadores == True):
            
            #Variables para los resultados de la semana
            i = 1
            total = 0
            nombre_ganador = "indefinido"
            cedula_ganador = 0
            monto_ganador = 0

            #Ciclo que recorre los cien participantes
            while(i <= 100):
                #Solicitud de variables locales
                print("Participante #", i)
                print("Ingrese su nombre: ")
                nombre = input(">>")
                print("Ingrese su Cédula:")
                cedula = input(">>")
                cedula = int(cedula)
                print("Ingrese el monto a aportar: 500/1000/2000/5000")
                monto = input(">>")
                monto = int(monto)

                if(monto == 500 or monto == 1000 or monto == 2000 or monto == 5000):
                    if (i == ganador_semana3):
                        nombre_ganador = nombre
                        cedula_ganador = cedula
                        monto_ganador = monto
                    i += 1
                    total += monto
                else:
                    print("Ingrese valores correctos")

            #Impresión de resultados de la semana
            print("El ganador de la semana #3 es:")
            print("Nombre: ", nombre_ganador)
            print("Cédula: ", cedula_ganador)
            #Determina el premio
            if(monto_ganador == 500):
                print("Usted se ha ganado una hamburguesa con papas y gaseosa")
            if(monto_ganador == 1000):
                print("Usted se ha ganado un cupon de cena para 2 personas")
            if(monto_ganador == 2000):
                print("Usted se ha ganado un día en el parque de diversiones con transporte y comida pago para 3 personas")
            if(monto_ganador == 5000):
                print("Usted se ha ganado un fin de semana todo incluido en hotel paradisiaco para 2 personas")
            #Imprime el total de la semana
            print("Total de la semana #3: ", total)
            
        else:
            print("No se han ingresado ganadores")
            condicional()
            
    elif op == 5:
        print("Semana #4")
        
        #Verifica si ya se han ingresado ganadores
        if (paso_ganadores == True):
            #Variables para los resultados de la semana
            i = 1
            total = 0
            nombre_ganador = "indefinido"
            cedula_ganador = 0
            monto_ganador = 0

            #Ciclo que recorre los cien participantes
            while(i <= 100):
                #Solicitud de variables locales
                print("Participante #", i)
                print("Ingrese su nombre: ")
                nombre = input(">>")
                print("Ingrese su Cédula:")
                cedula = input(">>")
                cedula = int(cedula)
                print("Ingrese el monto a aportar: 500/1000/2000/5000")
                monto = input(">>")
                monto = int(monto)

                if(monto == 500 or monto == 1000 or monto == 2000 or monto == 5000):
                    if (i == ganador_semana4):
                        nombre_ganador = nombre
                        cedula_ganador = cedula
                        monto_ganador = monto
                    i += 1
                    total += monto
                else:
                    print("Ingrese valores correctos")

            #Impresión de resultados de la semana
            print("El ganador de la semana #2 es:")
            print("Nombre: ", nombre_ganador)
            print("Cédula: ", cedula_ganador)
            #Determina el premio
            if(monto_ganador == 500):
                print("Usted se ha ganado una hamburguesa con papas y gaseosa")
            if(monto_ganador == 1000):
                print("Usted se ha ganado un cupon de cena para 2 personas")
            if(monto_ganador == 2000):
                print("Usted se ha ganado un día en el parque de diversiones con transporte y comida pago para 3 personas")
            if(monto_ganador == 5000):
                print("Usted se ha ganado un fin de semana todo incluido en hotel paradisiaco para 2 personas")
            #Imprime el total de la semana
            print("Total de la semana #4: ", total)
            
        else:
            print("No se han ingresado ganadores")
            condicional()
        
        
    elif op == 6:
        print("Ha salido exitosamente")
    else:
        print("Ingrese una opción correcta")
        op = menu()

#Llama a la función
condicional()


