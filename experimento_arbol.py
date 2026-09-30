"""
SABORBOT — EXPERIMENTO TP3: Búsqueda Secuencial O(N) vs. Árbol Binario O(log N)

Complementa experimento.py (TP2, que comparó secuencial vs. binaria sobre
lista ordenada). Acá el contendiente es la estructura del TP3: el ABB de
estructuras/arbol.py. A diferencia de la búsqueda binaria, el árbol no
necesita reordenar nada tras cada inserción.
"""

import time
import random

from modelos.receta import Receta
from algoritmos.busqueda import buscar_exacta_secuencial
from estructuras.arbol import ArbolBST


def crear_recetas_ficticias(cantidad):
    """Mismo generador que experimento.py, pero mezclando el orden final:
    si insertáramos los nombres ya ordenados (Receta_000000, Receta_000001...)
    el árbol degeneraría en una lista enlazada (altura = n). Con orden
    aleatorio, el árbol queda razonablemente balanceado (caso promedio)."""
    recetas = []
    for i in range(cantidad):
        nombre = f"Receta_{i:06d}"
        recetas.append(
            Receta(
                id_receta=i,
                nombre=nombre,
                categoria="Plato Principal",
                ingredientes=["carne", "papa", "huevo"],
                dificultad="media",
                valoracion=8.5,
            )
        )
    random.shuffle(recetas)
    return recetas


def correr_experimento():
    tamanos = [100, 1000, 10000, 50000]

    print("\n" + "=" * 70)
    print("      SABORBOT — EXPERIMENTO DE COMPLEJIDAD (TP3)")
    print("=" * 70)
    print(f"{'N Recetas':<12} | {'Secuencial O(N)':<18} | {'Árbol O(log N)':<18} | {'Altura':<8}")
    print("-" * 70)

    for n in tamanos:
        dataset = crear_recetas_ficticias(n)
        objetivo = dataset[-1].nombre  # peor caso para la búsqueda secuencial

        arbol = ArbolBST.construir_desde(dataset)

        t1 = time.perf_counter()
        _ = buscar_exacta_secuencial(dataset, objetivo)
        t2 = time.perf_counter()
        tiempo_sec = (t2 - t1) * 1000

        t1 = time.perf_counter()
        _ = arbol.buscar(objetivo)
        t2 = time.perf_counter()
        tiempo_arbol = (t2 - t1) * 1000

        print(f"{n:<12} | {tiempo_sec:>14.4f} ms | {tiempo_arbol:>14.4f} ms | {arbol.altura():<8}")

    print("=" * 70 + "\n")


if __name__ == "__main__":
    correr_experimento()
