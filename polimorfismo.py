
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('hola')
        print('Ando camiando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('ando moviendome en mi bicicleta')

def main():
    persona = Persona('Daniel')
    persona.avanza()

    cilista = Ciclista('pedro')
    cilista.avanza()

if __name__ == "__main__":
    main()