"""
Pruebas de estructuras/arbol.py (TP3).

Se corren con: python3 -m unittest tests.test_arbol -v
"""

import unittest

from modelos.receta import Receta
from estructuras.arbol import ArbolBST


def _receta(nombre, valoracion=8.0):
    return Receta(
        id_receta=nombre,
        nombre=nombre,
        categoria="plato principal",
        ingredientes=["papa", "sal"],
        dificultad="fácil",
        valoracion=valoracion,
    )


class TestArbolBST(unittest.TestCase):

    def setUp(self):
        self.nombres = ["Milanesa", "Flan", "Tarta", "Budín", "Provoleta", "Ensalada"]
        self.arbol = ArbolBST()
        for n in self.nombres:
            self.arbol.insertar(_receta(n))

    def test_insertar_incrementa_cantidad(self):
        self.assertEqual(len(self.arbol), len(self.nombres))

    def test_buscar_encuentra_existente(self):
        resultado = self.arbol.buscar("Flan")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Flan")

    def test_buscar_es_case_insensitive(self):
        resultado = self.arbol.buscar("mILANESA")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Milanesa")

    def test_buscar_no_existente_devuelve_none(self):
        self.assertIsNone(self.arbol.buscar("Pizza"))

    def test_buscar_en_arbol_vacio(self):
        self.assertIsNone(ArbolBST().buscar("cualquier cosa"))

    def test_inorder_devuelve_orden_alfabetico(self):
        nombres_inorder = [r.nombre for r in self.arbol.inorder()]
        self.assertEqual(nombres_inorder, sorted(self.nombres))

    def test_preorder_empieza_por_la_raiz(self):
        self.assertEqual(self.arbol.preorder()[0].nombre, "Milanesa")

    def test_postorder_termina_en_la_raiz(self):
        self.assertEqual(self.arbol.postorder()[-1].nombre, "Milanesa")

    def test_insertar_nombre_duplicado_no_duplica_cantidad(self):
        cantidad_previa = len(self.arbol)
        self.arbol.insertar(_receta("Flan", valoracion=10.0))
        self.assertEqual(len(self.arbol), cantidad_previa)
        self.assertEqual(self.arbol.buscar("Flan").valoracion, 10.0)

    def test_altura_arbol_vacio_es_cero(self):
        self.assertEqual(ArbolBST().altura(), 0)

    def test_altura_un_solo_nodo_es_uno(self):
        arbol = ArbolBST()
        arbol.insertar(_receta("Única"))
        self.assertEqual(arbol.altura(), 1)


if __name__ == "__main__":
    unittest.main()
