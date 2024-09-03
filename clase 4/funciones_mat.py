#funcioes matematicas
def suma (a,b):
    return a+b 
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b 
def divicion(a,b):
    if(b==0):
        return("no se puede dividir 0 pdj")
    else:
        return a/b
def raiz(a,b=2):
    return a**0.5

if __name__ == '__main__':
    print("la suma de 3 +2 es :",suma(3,2))
    print("raiz de 3:",raiz(5))
    print("la divicion de 4 con 2 es :",divicion(4,0))

