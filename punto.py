import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "origen"
        elif self.x > 0 and self.y > 0:
            return "primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "tercer cuadrante"
        else:
            return "cuarto cuadrante"
    
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


#Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
p1 = Punto(2, 3)
p2 = Punto(5, 5)
p3 = Punto(-3, 1)
p4 = Punto(0, 0)


#Consulta a que cuadrante pertenecen el punto A, C y D e imprimelos por pantalla.
print("El punto {0} se encuentra en el {1}".format(p1, p1.cuadrante()))
print("El punto {0} se encuentra en el {1}".format(p3, p3.cuadrante()))
print("El punto {0} se encuentra en el {1}".format(p4, p4.cuadrante()))
print("\n")

#Consulta los vectores AB y BA
p1p2= p1.vector(p2)
print("El vector entre {0} y {1} es {2}".format(p1, p2, p1p2))
p2p1= p2.vector(p1)
print("El vector entre {0} y {1} es {2}".format(p2, p1, p2p1))
print("\n")

#Consulta la distancia entre los puntos 'A y B' y 'B y A'. Comprueba el resultado anterior.
distp1p2 = p1.distancia(p2)
print("La distancia entre {0} y {1} es {2}".format(p1, p2, distp1p2))
distp2p1 = p2.distancia(p1)
print("La distancia entre {0} y {1} es {2}".format(p2, p1, distp2p1))
print("\n")

#Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0)
def masLejos(p1, p2, p3):
    distp1 = p1.distancia(Punto(0, 0))
    distp2 = p2.distancia(Punto(0, 0))
    distp3 = p3.distancia(Punto(0, 0))
    if distp1 > distp2 and distp1 > distp3:
        return p1
    elif distp2 > distp1 and distp2 > distp3:
        return p2
    else:
        return p3

print("El punto {0} se encuentra más lejos del origen".format(masLejos(p1, p2, p3)))
print("\n")

#Crea un rectángulo utilizando los puntos A y B.
rect = Rectangulo(p1, p2)
print("El rectángulo tiene una base de {0} y una altura de {1}".format(rect.base(), rect.altura()))
print("El área del rectángulo es {0}".format(rect.area()))

#Muestra por pantalla el rectangulo dibujado
import turtle
turtle.setup(400, 400)
#hacer el rectangulo mas grande
turtle.setworldcoordinates(-10, -10, 10, 10)
turtle.penup()
turtle.goto(p1.x, p1.y)
turtle.pendown()
turtle.goto(p2.x, p1.y)
turtle.goto(p2.x, p2.y)
turtle.goto(p1.x, p2.y)
turtle.goto(p1.x, p1.y)
turtle.done()
