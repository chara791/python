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




def buscarPalabrasOfencivas(url):
    contenido = ve_contenido(url)

    for po in lista:
        if po in contenido.decode():
            print(f"el insulto {po}  existe en el sitio")

    
   

url="https://www.revistagq.com/la-buena-vida/articulos/221-insultos-en-castellano-que-deberias-saber/19728"

#print(ve_contenido(url))

buscarPalabrasOfencivas(url)
    
S

