
class Coordenada:

    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    
    def distancia (self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2
        z_diff = (self.z - otra_coordenada.z)**2

        return (x_diff + y_diff +z_diff)**0.5

if __name__ == "__main__":
    coord_1 = Coordenada(3, 30, 0)
    coord_2 = Coordenada(4, 8, 0)

    # print(coord_1.distancia(coord_2))
    print(isinstance(coord_2, Coordenada))