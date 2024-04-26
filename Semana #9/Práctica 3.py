#Práctica #3 (Sinceramente que buen código me hice!! )

print("Programa que presenta los productos de la pulpería")

#Grupos
articulos_enlatados = []
productos_de_limpieza = []
carnes = []
granos = []

#Función para mostrar el grupo
def mostrar_grupo(grupo):
    if(grupo == []):
        print("\nEl grupo está vacío")#Por si está vacío
    else:
        largo = len(grupo)#Toma el tamaño del vector
        #Recorre el vector
        for i in range(largo):
            print(" - Producto #", i + 1 , ":", grupo[i])

#Funcion que verifica si un producto ya existe
def ya_esta(grupo,producto):

    #Variable que determina si ya está un producto
    determinante = False
    
    largo = len(grupo)#Toma el tamaño del vector
    #Recorre el vector
    for i in range(largo):
        if(grupo[i] == producto):
            determinante = True

    #Retorna el resultado de la función
    return determinante

#Función para agregar al grupo
def agregar_grupo(grupo):
    #Variables locales
    i = "si"
    producto = "indefinido"
    sino = "indefinido"

    while(i == "si" or i == "Si" or i == "SI"):
        print("\nIngrese el producto que desea agregar")
        producto = input(">>")

        if(ya_esta(grupo,producto) == True):
            print("\nEl producto ya existe")
        else:
            grupo.append(producto)#Agrega el producto al vector
            print("\nProducto agregado")
            mostrar_grupo(grupo)
            
        valido = False

        #Verifica la respuesta
        while(valido == False):
            #Consulta si desea continuar
            print("\n¿Desea seguir ingresando productos?\n")
            sino = input(">>")
            
            if(sino == "si" or sino == "Si" or sino == "SI"):
                print("Usted continuará ingresando\n")
                valido = True
            elif(sino == "no" or sino == "No" or sino == "NO"):
                print("Usted regresará al menú\n")
                i = "no"
                valido = True
            else:
                print("Escogió una opción inválida")

#Función para modificar al grupo
def modificar_grupo(grupo):
    mostrar_grupo(grupo)

    if(grupo == []):
        print("Usted regresará al menú\n")
    else:
        #Toma el largo del vector
        largo = len(grupo)
        
        #Variables para guardar el número y nuevo producto
        print("\nIngrese el número del producto que desea modificar: ")
        num_producto = int(input(">>"))

        #Verfica si se puede modificar
        if(num_producto > largo):
            print("No se puede agregar")
        else:
            print("Ingrese el producto al que va a cambiar: ")
            nuevo_producto = input(">>")

            #Reemplaza el producto
            grupo[num_producto - 1] = nuevo_producto

            #Muestra la modificación
            print("\nEl producto se modificó correctamente")
            mostrar_grupo(grupo)
            print("Usted regresará al menú\n")

#Función para eliminar del grupo
def eliminar_grupo(grupo):
    mostrar_grupo(grupo)

    if(grupo == []):
        print("Usted regresará al menú\n")
    else:
        #Toma el largo del vector
        largo = len(grupo)

        #Variables para guardar el número y nuevo producto
        print("\nIngrese el número del producto que desea eliminar: ")
        num_producto = int(input(">>"))

        #Verfica si se puede modificar
        if(num_producto > largo):
            print("No se puede eliminar")
        else:
            #Variable de consulta
            pregunta = "indefinido"

            valido = False

                #Verifica la respuesta
            while(valido == False):

                #Realiza la consulta
                print("\n¿Está seguro de eliminar el producto?")
                pregunta = input(">>")

                #Según la respuesta
                if(pregunta == "si" or pregunta == "Si" or pregunta == "SI"):
                    grupo.pop(num_producto - 1)#Elimina el elemento
                    print("El producto ha sido eliminado correctamente")
                    mostrar_grupo(grupo)
                    print("Usted regresará al menú\n")
                    valido = True
                elif(pregunta == "no" or pregunta == "No" or pregunta == "NO"):
                    print("Usted regresará al menú\n")
                    i = "no"
                    valido = True
                else:
                    print("Escogió una opción inválida")

#Función para devolver el grupo
def grupo():

    #Variable que determina si el valor es correcto
    determinante = True

    #Condicional que devuelve el grupo
    while(determinante == True):
        print("Ingrese el grupo que desea gestionar: ")
        print("1 - Articulos Enlatados")
        print("2 - Productos De Limpieza")
        print("3 - Carnes")
        print("4 - Granos")
        op = input(">>")

        if(op == "1"):
            determinante = False
            return(articulos_enlatados)
        elif(op == "2"):
            determinante = False
            return(productos_de_limpieza)
        elif(op == "3"):
            determinante = False
            return(carnes)
        elif(op == "4"):
            determinante = False
            return(granos)
        else:
            print("Ingrese una opción válida")
        
#Función que gestiona el menú
def menu():

    #Variable
    salir = "no"

    #Ciclo condicional del menu
    while(salir == "no"):
        print("Bienvenido al Menú")
        print("Ingrese la opción que desea: ")
        print("1 - Agregar")
        print("2 - Modificar")
        print("3 - Eliminar")
        print("4 - Salir")
        op = input(">>")

        if(op == "1"):
            agregar_grupo(grupo())
        elif(op == "2"):
            modificar_grupo(grupo())
        elif(op == "3"):
            eliminar_grupo(grupo())
        elif(op == "4"):
            print("Usted Saldrá correctamente")
            salir = "si"#Cambia la variable para salir
        else:
            print("Ha elegido una opción incorrecta")

#Invoca al menú
menu()

