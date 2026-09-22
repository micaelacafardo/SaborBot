import time
import random
from modelos.receta import Receta
from algoritmos.busqueda import buscar_por_nombre, busqueda_binaria_por_nombre


def crear_recetas_ficticias(cantidad):
    """Crea N recetas de prueba para medir el tiempo."""
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
                valoracion=8.5
            )
        )
    return recetas


def correr_experimento():
    tamanos = [100, 1000, 10000, 100000]

    print("\n" + "=" * 65)
    print("      SABORBOT — EXPERIMENTO DE COMPLEJIDAD (TP2)")
    print("=" * 65)
    print(f"{'N Recetas':<12} | {'Busq. Secuencial O(N)':<22} | {'Busq. Binaria O(log N)':<22}")
    print("-" * 65)

    for n in tamanos:
        # 1. Creamos N recetas
        dataset = crear_recetas_ficticias(n)

        # 2. Copia ordenada para la búsqueda binaria
        dataset_ordenado = sorted(dataset, key=lambda r: r.nombre.lower())

        # Receta a buscar (una del final para medir el peor caso)
        objetivo = f"Receta_{(n - 2):06d}"

        # 3. Medimos Búsqueda Secuencial
        t1 = time.perf_counter()
        _ = buscar_por_nombre(dataset, objetivo)
        t2 = time.perf_counter()
        tiempo_sec = (t2 - t1) * 1000  # pasar a milisegundos

        # 4. Medimos Búsqueda Binaria
        t1 = time.perf_counter()
        _ = busqueda_binaria_por_nombre(dataset_ordenado, objetivo)
        t2 = time.perf_counter()
        tiempo_bin = (t2 - t1) * 1000  # pasar a milisegundos

        print(f"{n:<12} | {tiempo_sec:>18.4f} ms | {tiempo_bin:>18.4f} ms")

    print("=" * 65 + "\n")


if __name__ == "__main__":
    correr_experimento()