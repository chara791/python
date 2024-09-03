class calculadora:
    numero1=None
    numero2=None
    resultado=None

    def __init__(self,x,y):
        self.numero1=x
        self.numero2=y
        resultado=0
    
    def sumar(self):
        self.resultado=self.numero1+self.numero2
        return self.resultado
    def resta(self):
       self.resultado=self.numero1-self.numero2
       return self.resultado
    def Setvaloes(self,x,y):
        self.numero1=x
        self.numero2=y
if __name__=="__main__":
    micasio= calculadora(10,30)
    print(f"la suma es:{micasio.sumar()}")
    print(f"la suma es:{micasio.resta()}")
micasio.Setvaloes(50,50)
print(f"la suma es:{micasio.sumar()}")
print(f"la suma es:{micasio.resta()}")
