"""Nota al Profesor:
La podía hacer más corta y menos tediosa, pero me di cuenta de como,
ya cuando la terminé y ya teniendo sueño :( """

#Práctica #2

print("Práctica #2")
print("Programa que presenta la temperatura promedio")

#Variables Booleanas
paso_lunes = False
paso_martes = False
paso_miercoles = False
paso_jueves = False
paso_viernes = False

#Definición del menú
def menu():
    print("Menú Principal")
    print("Seleccione el día que desea ingresar")
    print("[1] Lunes")
    print("[2] Martes")
    print("[3] Miércoles")
    print("[4] Jueves")
    print("[5] Viernes")
    print("[6] Mostrar Resultados y salir")
    op = int(input(">>"))
    return op

#Fin del menú

#Definición del condicional
def condicional():
    op = menu()
    if op == 1:

        #Variables (inicializadas)
        i = "si"
        global mayor_lunes
        mayor_lunes = 0
        global nombre_de_mayor_lunes
        global menor_lunes
        menor_lunes = 1000
        global nombre_de_menor_lunes
        global promedio_lunes
        promedio_lunes = 0
        global paso_lunes
        paso_lunes = True
        contador = 0
        
        while i == "si" or i == "SI" or i == "Si":

            #Solicitud de datos
            print("Ingrese su nombre:")
            nombre = input(">>")
            print("Ingrese su temperatura:")
            temp = input(">>")
            temp = int(temp)
            contador += 1
            promedio_lunes += temp

            #Si es mayor, menor
            if (temp <= menor_lunes):
                menor_lunes = temp
                nombre_de_menor_lunes = nombre
            if (temp >= mayor_lunes):
                mayor_lunes = temp
                nombre_de_mayor_lunes = nombre

            print("Desea continuar: si/no")
            i = input(">>")

        #Cálculo del promedio
        promedio_lunes /= contador
        if(menor_lunes == 1000):
            menor_lunes = 0

        #Retorna al condicional
        condicional()
        
    elif op == 2:

        #Variables (inicializadas)
        i = "si"
        global mayor_martes
        mayor_martes = 0
        global nombre_de_mayor_martes
        global menor_martes
        menor_martes = 1000
        global nombre_de_menor_martes
        global promedio_martes
        promedio_martes = 0
        global paso_martes
        paso_martes = True
        contador = 0
        
        while i == "si" or i == "SI" or i == "Si":

            #Solicitud de datos
            print("Ingrese su nombre:")
            nombre = input(">>")
            print("Ingrese su temperatura:")
            temp = input(">>")
            temp = int(temp)
            contador += 1
            promedio_martes += temp

            #Si es mayor, menor
            if (temp <= menor_martes):
                menor_martes = temp
                nombre_de_menor_martes = nombre
            if (temp >= mayor_martes):
                mayor_martes = temp
                nombre_de_mayor_martes = nombre

            print("Desea continuar: si/no")
            i = input(">>")

        #Cálculo del promedio
        promedio_martes /= contador
        if(menor_martes == 1000):
            menor_martes = 0

        #Retorna al condicional
        condicional()
        
    elif op == 3:

        #Variables (inicializadas)
        i = "si"
        global mayor_miercoles
        mayor_miercoles = 0
        global nombre_de_mayor_miercoles
        global menor_miercoles
        menor_miercoles = 1000
        global nombre_de_menor_miercoles
        global promedio_miercoles
        promedio_miercoles = 0
        global paso_miercoles
        paso_miercoles = True
        contador = 0
        
        while i == "si" or i == "SI" or i == "Si":

            #Solicitud de datos
            print("Ingrese su nombre:")
            nombre = input(">>")
            print("Ingrese su temperatura:")
            temp = input(">>")
            temp = int(temp)
            contador += 1
            promedio_miercoles += temp

            #Si es mayor, menor
            if (temp <= menor_miercoles):
                menor_miercoles = temp
                nombre_de_menor_miercoles = nombre
            if (temp >= mayor_miercoles):
                mayor_miercoles = temp
                nombre_de_mayor_miercoles = nombre

            print("Desea continuar: si/no")
            i = input(">>")

        #Cálculo del promedio
        promedio_miercoles /= contador
        if(menor_miercoles == 1000):
            menor_miercoles = 0

        #Retorna al condicional
        condicional()
        
    elif op == 4:
        
        #Variables (inicializadas)
        i = "si"
        global mayor_jueves
        mayor_jueves = 0
        global nombre_de_mayor_jueves
        global menor_jueves
        menor_jueves = 1000
        global nombre_de_menor_jueves
        global promedio_jueves
        promedio_jueves = 0
        global paso_jueves
        paso_jueves = True
        contador = 0
        
        while i == "si" or i == "SI" or i == "Si":

            #Solicitud de datos
            print("Ingrese su nombre:")
            nombre = input(">>")
            print("Ingrese su temperatura:")
            temp = input(">>")
            temp = int(temp)
            contador += 1
            promedio_jueves += temp

            #Si es mayor, menor
            if (temp <= menor_jueves):
                menor_jueves = temp
                nombre_de_menor_jueves = nombre
            if (temp >= mayor_jueves):
                mayor_jueves = temp
                nombre_de_mayor_jueves = nombre

            print("Desea continuar: si/no")
            i = input(">>")

        #Cálculo del promedio
        promedio_jueves /= contador
        if(menor_jueves == 1000):
            menor_jueves = 0

        #Retorna al condicional
        condicional()
        
    elif op == 5:

        #Variables (inicializadas)
        i = "si"
        global mayor_viernes
        mayor_viernes = 0
        global nombre_de_mayor_viernes
        global menor_viernes
        menor_viernes = 1000
        global nombre_de_menor_viernes
        global promedio_viernes
        promedio_viernes = 0
        global paso_viernes
        paso_viernes = True
        contador = 0
        
        while i == "si" or i == "SI" or i == "Si":

            #Solicitud de datos
            print("Ingrese su nombre:")
            nombre = input(">>")
            print("Ingrese su temperatura:")
            temp = input(">>")
            temp = int(temp)
            contador += 1
            promedio_viernes += temp

            #Si es mayor, menor
            if (temp <= menor_viernes):
                menor_viernes = temp
                nombre_de_menor_viernes = nombre
            if (temp >= mayor_viernes):
                mayor_viernes = temp
                nombre_de_mayor_viernes = nombre

            print("Desea continuar: si/no")
            i = input(">>")

        #Cálculo del promedio
        promedio_viernes /= contador
        if(menor_viernes == 1000):
            menor_viernes = 0

        #Retorna al condicional
        condicional()
        
    elif op == 6:
        
        print("opción 6")
        
        #Impresión del lunes
        if (paso_lunes == True):
            print("Lunes")
            print(" - Temperatura promedio: ", promedio_lunes)
            print(" - Temperatura máxima: ", mayor_lunes, " | ", nombre_de_mayor_lunes)
            print(" - Temperatura mínima: ", menor_lunes, " | ", nombre_de_menor_lunes)
        else:
            print("No hay datos que mostrar el Lunes")

        #Impresión del martes
        if (paso_martes == True):
            print("Martes")
            print(" - Temperatura promedio: ", promedio_martes)
            print(" - Temperatura máxima: ", mayor_martes, " | ", nombre_de_mayor_martes)
            print(" - Temperatura mínima: ", menor_martes, " | ", nombre_de_menor_martes)
        else:
            print("No hay datos que mostrar el Martes")
        
        #Impresión del miercoles
        if (paso_miercoles == True):
            print("Miércoles")
            print(" - Temperatura promedio: ", promedio_miercoles)
            print(" - Temperatura máxima: ", mayor_miercoles, " | ", nombre_de_mayor_miercoles)
            print(" - Temperatura mínima: ", menor_miercoles, " | ", nombre_de_menor_miercoles)
        else:
            print("No hay datos que mostrar el Miércoles")
        
        #Impresión del jueves
        if (paso_jueves == True):
            print("Jueves")
            print(" - Temperatura promedio: ", promedio_jueves)
            print(" - Temperatura máxima: ", mayor_jueves, " | ", nombre_de_mayor_jueves)
            print(" - Temperatura mínima: ", menor_jueves, " | ", nombre_de_menor_jueves)
        else:
            print("No hay datos que mostrar el Jueves")
        
        #Impresión del viernes
        if (paso_viernes == True):
            print("viernes")
            print(" - Temperatura promedio: ", promedio_viernes)
            print(" - Temperatura máxima: ", mayor_viernes, " | ", nombre_de_mayor_viernes)
            print(" - Temperatura mínima: ", menor_viernes, " | ", nombre_de_menor_viernes)
        else:
            print("No hay datos que mostrar el Viernes")
         
    else:
        
        print("Usted ha seleccionado una opción incorrecta")
        menu()

#Fin del condicional
condicional()
