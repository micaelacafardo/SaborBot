import unittest
from estructuras.grafo import Grafo
from algoritmos.bfs import bfs
from algoritmos.dfs import dfs

class TestRecorridos(unittest.TestCase):
    def setUp(self):
        self.g = Grafo()
        # A - B - C
        # |
        # D
        self.g.agregar_arista("A", "B")
        self.g.agregar_arista("B", "C")
        self.g.agregar_arista("A", "D")

    def test_bfs_distancias(self):
        orden, dist = bfs(self.g, "A")
        self.assertEqual(dist["A"], 0)
        self.assertEqual(dist["B"], 1)
        self.assertEqual(dist["D"], 1)
        self.assertEqual(dist["C"], 2)

    def test_dfs_visita_todos(self):
        orden = dfs(self.g, "A")
        self.assertEqual(set(orden), {"A", "B", "C", "D"})
        self.assertEqual(len(orden), 4)

if __name__ == "__main__":
    unittest.main()