import random
class pokemon:
    def __init__(self,nombre,tipo,vida=100,evolucion=1):
        self.ataque=[]
        self.vida=vida
        self.nombre=nombre
        self.tipo=tipo
        self.evolucion=evolucion
    def setAtaque(self,ataque):
        self.ataque.append(ataque)
    def atacar(self,i):
        return(f"{self.nombre}ataco con {self.ataque[i]}")
    def defenderse(self):
        return(f"{self.nombre} se defendio")
if __name__=="__main__":
    pikachu=pokemon(tipo="electrico",nombre="pikachu",vida=200)
    vaporeon=pokemon(tipo="agua",nombre="vaporeon",vida=300 ,evolucion=1)
    pikachu.setAtaque("inpactrueno")
    pikachu.setAtaque("rafaga")
    pikachu.setAtaque("cola de hierro")
    print(pikachu.atacar(0))
    print(vaporeon.defenderse())