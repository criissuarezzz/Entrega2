import copy
import unittest
import csv
import config
import database as db
import helpers

class TestDatabase(unittest.TestCase):
    def test_crear_punto(self):
        punto = db.Punto(1, 2)
        self.assertEqual(punto.x, 1)
        self.assertEqual(punto.y, 2)
        self.assertEqual(str(punto), "(1, 2)")
        self.assertEqual(punto.cuadrante(), "primer cuadrante")
        punto = db.Punto(-1, 2)
        self.assertEqual(punto.cuadrante(), "segundo cuadrante")
    
    def test_vector(self):
        punto1 = db.Punto(1, 2)
        punto2 = db.Punto(2, 3)
        vector = punto1.vector(punto2)
        self.assertEqual(vector.x, 1)
        self.assertEqual(vector.y, 1)

    def test_distancia(self):
        punto1 = db.Punto(1, 2)
        punto2 = db.Punto(2, 3)
        self.assertEqual(punto1.distancia(punto2), 1.4142135623730951)
    
    def test_crear_rectangulo(self):
        punto1 = db.Punto(1, 2)
        punto2 = db.Punto(2, 3)
        rectangulo = db.Rectangulo(punto1, punto2)
        self.assertEqual(rectangulo.base(), 1)
        self.assertEqual(rectangulo.altura(), 1)
        self.assertEqual(rectangulo.area(), 1)
