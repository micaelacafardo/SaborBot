import unittest
from estructuras.arbol_n_ario import ArbolNArio, NodoNArio


class TestArbolNArio(unittest.TestCase):

    def setUp(self):
        self.arbol = ArbolNArio("Gastronomía")
        
        principales = self.arbol.raiz.agregar_hijo(NodoNArio("Platos Principales"))
        principales.agregar_hijo(NodoNArio("Carnes"))
        principales.agregar_hijo(NodoNArio("Pastas"))
        
        postres = self.arbol.raiz.agregar_hijo(NodoNArio("Postres"))
        postres.agregar_hijo(NodoNArio("Helados"))

    def test_buscar_nodo_existente(self):
        resultado = self.arbol.buscar("Carnes")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.valor, "Carnes")

    def test_buscar_nodo_inexistente(self):
        resultado = self.arbol.buscar("Sushi")
        self.assertIsNone(resultado)

    def test_recorrido_preorden(self):
        recorrido = self.arbol.recorrer_preorden()
        esperado = ["Gastronomía", "Platos Principales", "Carnes", "Pastas", "Postres", "Helados"]
        self.assertEqual(recorrido, esperado)


if __name__ == "__main__":
    unittest.main()