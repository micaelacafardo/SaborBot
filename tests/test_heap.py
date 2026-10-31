import random
import unittest

from estructuras.heap import Heap
from servicios.ranking import top_n, prioridad


class TestHeap(unittest.TestCase):
    def test_extrae_en_orden_descendente(self):
        datos = [random.randint(0, 1000) for _ in range(200)]
        h = Heap()
        for d in datos:
            h.insertar(d)
        self.assertEqual([h.extraer() for _ in range(len(datos))],
                         sorted(datos, reverse=True))

    def test_min_heap(self):
        h = Heap.desde_lista([5, 1, 9, 3], max_heap=False)
        self.assertEqual(h.extraer(), 1)

    def test_heapify_equivale_a_insertar(self):
        datos = [random.random() for _ in range(100)]
        h = Heap.desde_lista(datos)
        self.assertEqual([h.extraer() for _ in range(100)],
                         sorted(datos, reverse=True))

    def test_vacio_lanza_error(self):
        with self.assertRaises(IndexError):
            Heap().extraer()
        with self.assertRaises(IndexError):
            Heap().ver_raiz()

    def test_ver_raiz_no_saca(self):
        h = Heap.desde_lista([1, 7, 3])
        self.assertEqual(h.ver_raiz(), 7)
        self.assertEqual(len(h), 3)


class TestRanking(unittest.TestCase):
    RECETAS = [
        {"nombre": "A", "categoria": "postre", "dificultad": "baja", "valoracion": 9.0, "tiempo_min": 30},
        {"nombre": "B", "categoria": "postre", "dificultad": "alta", "valoracion": 9.0, "tiempo_min": 30},
        {"nombre": "C", "categoria": "entrada", "dificultad": "baja", "valoracion": 7.0, "tiempo_min": 10},
    ]

    def test_top_n_ordena_por_prioridad(self):
        self.assertEqual([r["nombre"] for r in top_n(self.RECETAS, 3)], ["A", "B", "C"])

    def test_n_mayor_que_cantidad(self):
        self.assertEqual(len(top_n(self.RECETAS, 50)), 3)

    def test_filtro_categoria(self):
        self.assertEqual([r["nombre"] for r in top_n(self.RECETAS, 5, "entrada")], ["C"])

    def test_dificultad_penaliza(self):
        self.assertGreater(prioridad(self.RECETAS[0]), prioridad(self.RECETAS[1]))

    def test_receta_objeto_sin_tiempo(self):
        class Receta:
            nombre, categoria = "X", "postre"
            dificultad, valoracion = "baja", 8.0
        self.assertAlmostEqual(prioridad(Receta()), 8.0)


if __name__ == "__main__":
    unittest.main()
