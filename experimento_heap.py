"""Compara Top-N con heap vs ordenar todo (para justificar el heap en la defensa)."""
import random
import time

from servicios.ranking import top_n, prioridad


def generar(n):
    dif = ["baja", "media", "alta"]
    return [{"nombre": f"receta {i}", "categoria": "x",
             "dificultad": random.choice(dif),
             "valoracion": round(random.uniform(1, 10), 1),
             "tiempo_min": random.randint(5, 180)} for i in range(n)]


def con_ordenamiento(recetas, n):
    return sorted(recetas, key=prioridad, reverse=True)[:n]


def medir(f, *args, repeticiones=5):
    t0 = time.perf_counter()
    for _ in range(repeticiones):
        f(*args)
    return (time.perf_counter() - t0) / repeticiones * 1000


if __name__ == "__main__":
    print(f"{'N elementos':>12} | {'Heap Top-10 (ms)':>17} | {'Ordenar todo (ms)':>18}")
    for tam in (1_000, 10_000, 100_000):
        datos = generar(tam)
        print(f"{tam:>12} | {medir(top_n, datos, 10):>17.2f} | {medir(con_ordenamiento, datos, 10):>18.2f}")
