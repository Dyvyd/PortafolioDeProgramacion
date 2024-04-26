#Práctica #1 - Deivid Rojas Bolaños

print("Práctica #1")

#Entrada
print("Triángulo (T) o Cuadrado (C)")
figura = input("Ingrese una figura: ")

#Condicional en caso de triángulo, cuadrado o nulo
if(figura == "C" or figura == "c"):
    #Entrada
    lado = input("Ingrese la medida del lado del cuadrado: ")
    lado = int(lado)

    #Cálculo
    area = lado ** 2
    perimetro = lado * 4

    #Impresión
    print("El área del cuadrado es: ", area)
    print("El perímetro del cuadrado es: ", perimetro)
else:
    if(figura == "T" or figura == "t"):
        #Entrada
        base = input("Ingrese la medida de la base del triángulo: ")
        base = int(base)
        altura = input("Ingrese la medida de la altura del triángulo: ")
        altura = int(altura)
        hipotenusa = input("Ingrese la medida de la hipotenusa del triángulo: ")
        hipotenusa = int(hipotenusa)

        #Cálculo
        area = base * altura / 2
        perimetro = base + altura + hipotenusa

        #Impresión
        print("El área del triángulo es: ", area)
        print("El perímetro del triángulo es: ", perimetro)
    else:
        print("Ingrese una entrada válida(c o t)")
