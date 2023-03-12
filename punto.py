import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "El punto se encuentra en el origen"
        elif self.x > 0 and self.y > 0:
            return "El punto se encuentra en el primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "El punto se encuentra en el segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "El punto se encuentra en el tercer cuadrante"
        else:
            return "El punto se encuentra en el cuarto cuadrante"
    
    def vector(self, punto):
        return Punto(punto.x - self.x, punto.y - self.y)

    def distancia(self, punto):
        return math.sqrt((punto.x - self.x)**2 + (punto.y - self.y)**2)

class Rectangulo:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def base(self):
        return self.p1.distancia(Punto(self.p2.x, self.p1.y))
    def altura(self):
        return self.p1.distancia(Punto(self.p1.x, self.p2.y))
    def area(self):
        return self.base() * self.altura()
    