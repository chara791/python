class Rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def area(self):
        return self.base*self.altura
    def perimetro(self):
        return (self.base+self.altura)*2
    
class Cuadrado(Rectangulo):
    def __init__(self,lado):
        super().__init__(lado,lado)

if __name__=="__main__":
    rectangulo=Rectangulo(base=3,altura=4)
    print(rectangulo.area())

    cuadrado=Cuadrado(lado=5)
    print (cuadrado.area())

    cuadrado=Cuadrado(10)
    print (cuadrado.perimetro())