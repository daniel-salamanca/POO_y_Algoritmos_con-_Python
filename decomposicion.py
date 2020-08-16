
class  Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4)
        self._direccion = Direccion( movimiento="left", velocidad=50)

    def acelerar(self,tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'en_movimiento' 

    def realiza_movimiento(self, vuelta= False):
        if vuelta == True:
            self._direccion.direccion_de_movimiento("left", 50)
        else:
            self._direccion.direccion_de_movimiento(None, 10)
                    

class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros=cilindros
        self.tipo =tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        print("ahsiquhs")

class Direccion:

    def __init__(self, movimiento, velocidad = 0):
        self.movimiento = movimiento


    def direccion_de_movimiento (self, movimiento, velocidad):

        if movimiento == "left":
            print("El automovil se esta moviendo a la izquierda ")
            velocidad = velocidad - 10
        elif movimiento == "right":
            print("El automovil se esta moviendo a la derecha ")
            velocidad = velocidad - 10
        else:
            print("El automovil está en movimiento  ")            