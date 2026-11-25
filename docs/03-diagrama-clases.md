# Diagrama de Clases UML Completo — SaborBot

## Arquitectura por Capas
El sistema se divide en cinco capas desacopladas:
1. **Modelos (`modelos/`):** entidades del dominio (`Receta`, `Usuario`).
2. **Estructuras de Datos (`estructuras/`):** implementaciones propias sin librerías externas (`ArbolBST`, `ArbolAVL`, `ArbolNario`, `Heap`, `Grafo`).
3. **Algoritmos (`algoritmos/`):** búsquedas y recorridos sobre grafos (`bfs`, `dfs`).
4. **Servicios (`servicios/`):** casos de uso de negocio (ranking Top-N, recomendaciones por similitud y exploración BFS/DFS).
5. **Interfaz (`ui/`):** controlador de consola (`TerminalUI` en `ui/terminal.py`) con *dispatch table*.

```mermaid
classDiagram
    direction TB

    %% --- CAPA DE MODELOS ---
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

    %% --- CAPA DE ESTRUCTURAS DE DATOS ---
    class ArbolBST {
        -NodoBST _raiz
        +insertar(clave: str, receta: Receta) None
        +buscar(clave: str) Receta
        +inorden() list~Receta~
    }

    class ArbolAVL {
        -NodoAVL _raiz
        +insertar(clave: str, receta: Receta) None
        +buscar(clave: str) Receta
        -rotar_izquierda(nodo) NodoAVL
        -rotar_derecha(nodo) NodoAVL
    }

    class ArbolNario {
        -NodoNario _raiz
        +insertar_categoria(padre: str, categoria: str) None
        +agregar_receta(categoria: str, receta: Receta) None
        +listar_jerarquia() list
    }

    class Heap {
        -list _datos
        -bool _es_max
        +insertar(prioridad: float, item: Receta) None
        +extraer() tuple
        +esta_vacio() bool
        +__len__() int
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

    %% --- CAPA DE SERVICIOS Y ALGORITMOS ---
    class ServicioRanking {
        +calcular_puntaje(receta: Receta) float
        +obtener_top_n(recetas: list~Receta~, n: int, categoria: str) list
    }

    class RecomendadorGrafos {
        +construir_grafo_recetas(recetas: list~Receta~) Grafo
        +recomendar_similares(receta: Receta, grafo: Grafo, top_n: int) list
    }

    class RecorridosGrafos {
        +explorar_cercanas_bfs(receta: Receta, grafo: Grafo, nivel_max: int) dict
        +explorar_cadena_dfs(receta: Receta, grafo: Grafo) list
    }

    class AlgoritmosGrafos {
        <<module>>
        +bfs(grafo: Grafo, inicio: Receta) tuple
        +dfs(grafo: Grafo, inicio: Receta) list
    }

    %% --- CAPA DE INTERFAZ ---
    class TerminalUI {
        -list~Receta~ _recetas
        -Grafo _grafo
        -dict _opciones
        +ejecutar() None
        +mostrar_menu() None
    }

    %% --- RELACIONES ---
    TerminalUI --> Receta : gestiona catálogo
    TerminalUI ..> ArbolBST : consulta
    TerminalUI ..> ArbolAVL : consulta
    TerminalUI ..> ArbolNario : explora categorías
    TerminalUI ..> ServicioRanking : solicita Top-N
    TerminalUI ..> RecomendadorGrafos : solicita similares
    TerminalUI ..> RecorridosGrafos : ejecuta BFS/DFS

    ArbolBST "1" --> "*" Receta : indexa
    ArbolAVL "1" --> "*" Receta : indexa balanceado
    ArbolNario "1" --> "*" Receta : agrupa por categoría
    Grafo "1" --> "*" Receta : vértices y aristas

    ServicioRanking ..> Heap : usa para Top-N
    ServicioRanking ..> Receta : evalúa
    RecomendadorGrafos ..> Grafo : construye y consulta
    RecorridosGrafos ..> Grafo : recorre
    RecorridosGrafos ..> AlgoritmosGrafos : invoca bfs / dfs