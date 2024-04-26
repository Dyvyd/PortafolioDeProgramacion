#Game Of Progra

print("Game Of Progra")
print("Programa que presenta la cantidad de estudiantes nacidos en cada mes")

#Variables
promedio = 0
contador_de_edad = 0
contador_enero = 0
contador_febrero = 0
contador_marzo = 0
contador_abril = 0
contador_mayo = 0
contador_junio = 0
contador_julio = 0
contador_agosto = 0
contador_setiembre = 0
contador_octubre = 0
contador_noviembre = 0
contador_diciembre = 0
i = "si"

while i == "si":
    edad = input("Ingrese la edad del alumno: ")
    edad = int(edad)
    contador_de_edad += 1
    mes = input("Ingrese el mes del alumno: ")
    #Saca el mes en el que nació
    if (mes == "enero" or mes == "Enero" or mes == "ENERO"):
        contador_enero += 1
    elif (mes == "febrero" or mes == "Febrero" or mes == "FEBRERO"):
        contador_febrero += 1
    elif (mes == "marzo" or mes == "Marzo" or mes == "MARZO"):
        contador_marzo += 1
    elif (mes == "abril" or mes == "Abril" or mes == "ABRIL"):
        contador_abril += 1
    elif (mes == "mayo" or mes == "Mayo" or mes == "MAYO"):
        contador_mayo += 1
    elif (mes == "junio" or mes == "Junio" or mes == "JUNIO"):
        contador_junio += 1
    elif (mes == "Julio" or mes == "Julio" or mes == "Julio"):
        contador_julio += 1
    elif (mes == "agosto" or mes == "Agosto" or mes == "AGOSTO"):
        contador_agosto += 1
    elif (mes == "setiembre" or mes == "Setiembre" or mes == "SETIEMBRE"):
        contador_setiembre += 1
    elif (mes == "octubre" or mes == "Octubre" or mes == "OCTUBRE"):
        contador_octubre += 1
    elif (mes == "noviembre" or mes == "Noviembre" or mes == "NOVIEMBRE"):
        contador_noviembre += 1
    elif (mes == "diciembre" or mes == "Diciembre" or mes == "DICIEMBRE"):
        contador_diciembre += 1
    #Acumula las edades
    promedio += edad
    i = input("¿Desea continuar? si / no ")

promedio /= contador_de_edad
print("El promedio de las edades es: ", promedio)
print("La cantidad de alumnos de enero son: ", contador_enero)
print("La cantidad de alumnos de febrero son: ", contador_febrero)
print("La cantidad de alumnos de marzo son: ", contador_marzo)
print("La cantidad de alumnos de abril son: ", contador_abril)
print("La cantidad de alumnos de mayo son: ", contador_mayo)
print("La cantidad de alumnos de junio son: ", contador_junio)
print("La cantidad de alumnos de julio son: ", contador_julio)
print("La cantidad de alumnos de agosto son: ", contador_agosto)
print("La cantidad de alumnos de setiembre son: ", contador_setiembre)
print("La cantidad de alumnos de octubre son: ", contador_octubre)
print("La cantidad de alumnos de noviembre son: ", contador_noviembre)
print("La cantidad de alumnos de diciembre son: ", contador_diciembre)



