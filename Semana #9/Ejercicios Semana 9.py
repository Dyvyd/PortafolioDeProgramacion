ganadores = []

def mostrar_ganadores(ganadores_parametro):
    largo = len(ganadores_parametro)
    print("El largo de la lista es: ", largo)
    for i in range(largo):
        print("El ganador", i + 1, "es", ganadores[i])

mostrar_ganadores(ganadores)

print("\n Nueva Lista \n")

ganadores.append(96)
ganadores.append(73)
ganadores.append(71)
ganadores.append(64)
ganadores.append(90)

mostrar_ganadores(ganadores)

print("El largo es: ", len("patria"))

palabra = "patria"
# Obtenemos el largo de la palabra
largo_palabra = len(palabra)

print("La última letra es: ", palabra[-1])
