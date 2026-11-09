import unittest
from estructuras.grafo import Grafo
from servicios.recomendador_grafos import construir_grafo_recetas, recomendar_similares

class RecetaMock:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes
    def __repr__(self):
        return self.nombre

class TestGrafo(unittest.TestCase):
    def test_grafo_basico(self):
        g = Grafo()
        g.agregar_arista("A", "B", peso=3)
        self.assertTrue(g.existe_vertice("A"))
        self.assertEqual(g.obtener_vecinos("A"), {"B": 3})
        self.assertEqual(g.obtener_vecinos("B"), {"A": 3})
        self.assertEqual(len(g), 2)

    def test_construccion_y_recomendacion(self):
        r1 = RecetaMock("Milanesa", ["carne", "pan rallado", "huevo"])
        r2 = RecetaMock("Suprema", ["pollo", "pan rallado", "huevo"])
        r3 = RecetaMock("Ensalada", ["lechuga", "tomate"])
        
        grafo = construir_grafo_recetas([r1, r2, r3])
        
        # Milanesa y Suprema comparten "pan rallado" y "huevo" (peso 2)
        similares_mila = recomendar_similares(r1, grafo)
        self.assertEqual(len(similares_mila), 1)
        self.assertEqual(similares_mila[0][0].nombre, "Suprema")
        self.assertEqual(similares_mila[0][1], 2)
        
        # Ensalada no comparte nada con Milanesa
        self.assertEqual(recomendar_similares(r3, grafo), [])

if __name__ == "__main__":
    unittest.main()