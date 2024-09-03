claificaciones=[2,5,5,4.5,1]
nombres=["moieses","camila","fernanda","pablo","nadia"]
listaVariada=[True,10.5,"abc",[0,1,1]]

print("estudiante:",nombres[2])
print("calificacion:",claificaciones[-2])
print("lista dentro de otra",listaVariada[3][0])
print("inprimir un rango slices",nombres[1:2])
print(listaVariada)

#agregar elemntos a una lista 
nombres.append("anival")
print(nombres)
#remover elemtos 
nombres.remove("pablo")
print(nombres)