class perosona:
    def __init__(self,noombre):
        self.nombre=noombre

    def avanza(self):
        print('ando caminando con un flow violento')

class cliclista(perosona):
    def __init__(self, noombre):
        super().__init__(noombre)
    def avanza(self):
        print('ndo moviendome en bicicleta')

if __name__=="__main":
    perosona=('pepe')
    perosona.avanza()

    cliclista= cliclista('juaca')
    cliclista.avanza()