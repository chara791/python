import os

texto=input('Ingrese un texto a guardar')
nombreFichero= "archivo.txt"
f= open (nombreFichero,"a")
f.write(texto)
f.write("\n")
f.close()