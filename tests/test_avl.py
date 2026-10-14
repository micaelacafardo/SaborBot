import unittest
from modelos.receta import Receta
from estructuras.avl import ArbolAVL


def _receta(nombre: str) -> Receta:
    return Receta(
        id_receta=nombre,
        nombre=nombre,
        categoria="Prueba",
        ingredientes=["ingrediente1"],
        dificultad="fácil",
        valoracion=8.0
    )


class TestArbolAVL(unittest.TestCase):

    def test_auto_balanceo_orden_alfabetico(self):
        """Verifica que al insertar datos ya ordenados, el AVL no degenera a lista."""
        nombres = ["Ajo", "Banana", "Cebolla", "Durazno", "Ensalada", "Flan", "Guiso"]
        avl = ArbolAVL()
        for n in nombres:
            avl.insertar(_receta(n))

        # En un BST común la altura sería 7. En AVL no debe superar 3 o 4.
        self.assertLess(avl.altura(), 5)

    def test_buscar_existente(self):
        avl = ArbolAVL()
        avl.insertar(_receta("Milanesa"))
        resultado = avl.buscar("Milanesa")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Milanesa")

    def test_buscar_case_insensitive(self):
        avl = ArbolAVL()
        avl.insertar(_receta("Milanesa"))
        resultado = avl.buscar("mILANESA")
        self.assertIsNotNone(resultado)

    def test_inorder_devuelve_ordenado(self):
        nombres = ["Milanesa", "Ajo", "Tarta", "Budín"]
        avl = ArbolAVL()
        for n in nombres:
            avl.insertar(_receta(n))

        resultado = [r.nombre for r in avl.inorder()]
        self.assertEqual(resultado, sorted(nombres))


if __name__ == "__main__":
    unittest.main()