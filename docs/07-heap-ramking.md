# TP6 — Heap y ranking de recetas

Integrado al menú como **opción 8 — Ver Top-N de recetas (Heap)** (`ui/terminal.py`).

## ¿Qué problema resuelve?
El usuario quiere ver rápido las **mejores recetas** (Top N), opcionalmente filtradas por categoría.

## Función de prioridad
`puntaje = valoracion - 0.3 * nivel_dificultad - 0.5 * (tiempo_min / 60)`

- `nivel_dificultad`: baja = 0, media = 1, alta = 2.
- Una receta muy valorada pero difícil y larga queda por debajo de una igual de valorada y simple.
- Si una receta no tiene el campo `tiempo_min`, no se aplica la penalización por tiempo.
- Los pesos (`PESO_DIFICULTAD`, `PESO_TIEMPO`) están en `servicios/ranking.py` y se pueden ajustar.

## Implementación
- `estructuras/heap.py`: heap binaria implementada a mano sobre una lista (sin `heapq`).
  Operaciones: `insertar`, `extraer`, `ver_raiz`, `reemplazar_raiz`, `desde_lista` (heapify).
- `servicios/ranking.py`: `top_n` usa un **min-heap de tamaño N**. La raíz es la peor de las N mejores
  vistas; cada receta nueva solo entra si supera a la raíz.

## Complejidad
| Operación | Costo |
|---|---|
| insertar / extraer / reemplazar_raiz | O(log n) |
| ver_raiz | O(1) |
| desde_lista (heapify) | O(n) |
| Top-N con heap de tamaño N sobre m recetas | O(m log N), memoria O(N) |
| Top-N ordenando todo | O(m log m), memoria O(m) |

## ¿Por qué un heap y no ordenar todo?
Para N chico (10) y m grande, el heap mantiene solo N elementos y no necesita ordenar los m.
Además el ranking se puede mantener actualizado al agregar recetas nuevas sin reordenar todo.

## Experimento (`python3 experimento_heap.py`, Top-10)
| N recetas | Heap (ms) | Ordenar todo (ms) |
|---|---|---|
| 1.000 | 0.54 | 0.37 |
| 10.000 | 4.91 | 4.59 |
| 100.000 | 47.61 | 61.75 |

Conclusión: con pocos datos `sorted()` es igual o más rápido porque está implementado en C;
a medida que m crece, el heap gana por su complejidad O(m log N) y su menor memoria.
(Valores medidos en una máquina de prueba; los tuyos van a variar.)
