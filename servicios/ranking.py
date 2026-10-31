"""Ranking de recetas con Heap (TP6).

Función de prioridad: premia la valoración y penaliza un poco las recetas
difíciles y las que tardan mucho. Los pesos se pueden ajustar.
"""
from estructuras.heap import Heap

NIVEL_DIFICULTAD = {"baja": 0, "media": 1, "alta": 2}

PESO_DIFICULTAD = 0.3   # puntos que se restan por cada nivel de dificultad
PESO_TIEMPO = 0.5       # puntos que se restan por cada hora de preparación


_SIN_VALOR = object()


def _campo(receta, nombre, defecto=_SIN_VALOR):
    """Lee un campo tanto de un dict (JSON) como de un objeto con atributos."""
    if isinstance(receta, dict):
        if nombre in receta:
            return receta[nombre]
    else:
        for attr in (nombre, "_" + nombre):
            if hasattr(receta, attr):
                return getattr(receta, attr)
    if defecto is not _SIN_VALOR:
        return defecto
    raise AttributeError(f"la receta no tiene el campo '{nombre}'")


def prioridad(receta):
    """puntaje = valoración - penalización por dificultad - penalización por tiempo."""
    valoracion = float(_campo(receta, "valoracion"))
    dificultad = NIVEL_DIFICULTAD.get(str(_campo(receta, "dificultad")).lower(), 1)
    # Si la receta no guarda su tiempo, no se penaliza por tiempo.
    horas = float(_campo(receta, "tiempo_min", 0)) / 60
    return valoracion - PESO_DIFICULTAD * dificultad - PESO_TIEMPO * horas


def top_n(recetas, n=10, categoria=None, clave=prioridad):
    """Devuelve las N mejores recetas, de mayor a menor prioridad.

    Usa un MIN-heap de tamaño N: la raíz es la "peor" de las N mejores
    vistas hasta ahora. Cada receta nueva se compara con la raíz (O(1)) y
    solo entra al heap si la supera (O(log N)).
    Tiempo: O(m log N) con m recetas. Memoria extra: O(N).
    Ordenar todo costaría O(m log m) y O(m) de memoria.
    """
    if n <= 0:
        return []
    # Se guarda (puntaje, indice, receta): el puntaje se calcula UNA sola vez por receta.
    heap = Heap(clave=lambda t: (t[0], -t[1]), max_heap=False)
    for i, r in enumerate(recetas):
        if categoria is not None and str(_campo(r, "categoria")).lower() != categoria.lower():
            continue
        entrada = (clave(r), i, r)
        if len(heap) < n:
            heap.insertar(entrada)
        elif entrada[0] > heap.ver_raiz()[0]:
            heap.reemplazar_raiz(entrada)
    # El min-heap se vacía de peor a mejor: se invierte para mostrar el mejor primero.
    resultado = []
    while not heap.esta_vacio():
        resultado.append(heap.extraer()[2])
    resultado.reverse()
    return resultado


def mostrar_top(recetas, n=10, categoria=None):
    """Imprime el ranking en la terminal y devuelve la lista mostrada."""
    top = top_n(recetas, n, categoria)
    titulo = f"TOP {len(top)}" + (f" — {categoria}" if categoria else "")
    print("=" * 40)
    print(f"  {titulo}")
    print("=" * 40)
    if not top:
        print("  No hay recetas para mostrar.")
    medallas = {1: "🥇", 2: "🥈", 3: "🥉"}
    for i, r in enumerate(top, 1):
        icono = medallas.get(i, f"{i}.")
        print(f" {icono} {_campo(r, 'nombre'):<28} ⭐ {_campo(r, 'valoracion')}"
              f"  (puntaje {prioridad(r):.2f})")
    print("=" * 40)
    return top
