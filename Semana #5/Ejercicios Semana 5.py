"""rango = range (20)

print(rango)

for i in range(20):
    print("El elemento es: ", i)

lista = [1,2,3,70]

for elemento in lista:
    print("El elemento del conjunto es: ", elemento)

for i in range(5, 20):
    print("El elemento es: ", i)

valor = 20

while (valor > 0 and valor - 1 > 2):
    print("Multiplicando ", valor, " por 2: ", valor * 2)
    valor = valor -1
print("Salí del while")

entrada = input("Ingrese una entrada para ingresar al while a) ingresa b) sale ")

if entrada == "a":
    while entrada != "b":
        print("Usted ingresó al ciclo while ")
        entrada = input("¿Desea salir del ciclo? a) ingresa b) sale ")
        while entrada != "a" and entrada != "b":
            entrada = input("Ingrese una opción válida ")
elif entrada == "b":
    print("Elegiste la opción de no ingresar ")
else:
    print("Usteed ingresó una opción incorrecta ")"""
    
