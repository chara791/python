lista=[]

def cargar_lista(dato):
    lista.append(dato)


def cargar_lista(*argrs):
    for arg in argrs:
        lista.append(arg)

def imprimir_lista():
    for item in lista:
        print(item, end=' | ')

cargar_lista(25)
cargar_lista(50)
cargar_lista(75)
cargar_lista(100)

imprimir_lista()

cargar_lista('a','b','c',[125,852,963])
imprimir_lista()