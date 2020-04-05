from reto1 import *

#PROGRAMA PRINCIPAL
palabra = input("Introduzca la palabra bibliotecario :): ")
palabra_ca = [] #Dividiremos la palabra en letras
for i in palabra: 
    palabra_ca.append(i)
palabra_ca.append("\n")
cifrado_pal(palabra_ca)
