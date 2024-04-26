import os

archivo_prueba = open("text.txt","r")

"""archivo_prueba.write("Hola\n")
archivo_prueba.write("mundo")"""

entrada = archivo_prueba.read()
entrada_dividida = entrada.split("\n")

archivo_prueba.close()

print(entrada)
print(entrada_dividida)
