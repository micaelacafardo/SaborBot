# Diagrama de Clases UML — SaborBot (TP1)

## Notación UML Aplicada
- **Visibilidad:** `+` público, `-` privado (`_adyacencias` en Python).
- **Relaciones UML:**
  - **Dependencia (`..>`):** un módulo/servicio invoca o construye a otro sin mantenerlo como atributo permanente (por ejemplo, servicios que reciben un `Grafo` o usan `bfs` / `dfs`).
  - **Asociación (`-->`):** relación estructural entre clases (por ejemplo, `Grafo` relaciona vértices `Receta` y pesos de conexión).

```mermaid
classDiagram
    direction TB

    class Receta {
        +str nombre
        +str categoria
        +str dificultad
        +float valoracion
        +list~str~ ingredientes
        +tiene_ingrediente(ingrediente: str) bool
    }

    class Usuario {
        +str nombre
        +list~str~ preferencias
    }

    class Grafo {
        -dict _adyacencias
        +agregar_vertice(vertice: Receta) None
        +agregar_arista(origen: Receta, destino: Receta, peso: int) None
        +obtener_vecinos(vertice: Receta) dict
        +obtener_vertices() list
        +existe_vertice(vertice: Receta) bool
        +__len__() int
    }

    class RecomendadorGrafos {
        +construir_grafo_recetas(recetas: list~Receta~) Grafo
        +recomendar_similares(receta_objetivo: Receta, grafo: Grafo, top_n: int) list
    }

    class RecorridosGrafos {
        +explorar_cercanas_bfs(receta_inicio: Receta, grafo: Grafo, nivel_max: int) dict
        +explorar_cadena_dfs(receta_inicio: Receta, grafo: Grafo) list
    }

    Grafo "1" --> "*" Receta : vertices / aristas ponderadas
    RecomendadorGrafos ..> Grafo : construye y consulta
    RecomendadorGrafos ..> Receta : recomienda
    RecorridosGrafos ..> Grafo : aplica BFS y DFS
    RecorridosGrafos ..> Receta : explora