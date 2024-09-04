from urllib import request
from urllib.error import URLError
lista=["esta","el","carajo","Bellaco"]
def ve_contenido(url):
    try:
        f= request.urlopen(url)
    except URLError:
        return('¡laurl'+ url +'NO EXISTE')
    else:
        contenido=f.read()
        return contenido

def contar_palarbas(url):
    try:
        f=request.urlopen(url)
    except URLError:
        return('la url'+url+'no existe')
    else:
        contenido= f.read()
        return len(contenido.split())




    
   

url="https://www.revistagq.com/la-buena-vida/articulos/221-insultos-en-castellano-que-deberias-saber/19728"

#print(ve_contenido(url))

print(ve_contenido(url))
print("\n-------------------------------\n")
print(contar_palarbas(urlZ))
    

