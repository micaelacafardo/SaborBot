# SaborBot — Sistema Inteligente de Recomendación de Recetas

> **Trabajo Práctico Integrador**  
> **Materia:** Estructuras de Datos  
> **Institución:** Universidad Nacional Guillermo Brown (UNAB)  
> **Integrantes:** Jonathan Peralta, Micaela Cafardo  
> **Comisión:** 2 — **Grupo:** 28  
> **Dominio:** Gastronomía  

---

## 1. Descripción General y Dominio

**SaborBot** es un sistema inteligente de recomendación de recetas de cocina desarrollado en Python. Elegimos el dominio de la **gastronomía** porque ofrece relaciones complejas e interconexiones naturales que permiten aplicar de manera progresiva las estructuras de datos fundamentales de la materia:

- **Categorización:** Clasificación de recetas por tipo de plato (*entrada, plato principal, postre*).
- **Relaciones Complejas:** Conexión de recetas mediante ingredientes compartidos, base para el diseño de recomendaciones sobre grafos.
- **Escalabilidad y Rendimiento:** Evaluación empírica de algoritmos a medida que el volumen de datos aumenta.

---

## 2. Problema que Resuelve y Usuario Objetivo

Muchas personas saben qué ingredientes tienen en casa o disfrutan de una receta en particular, pero no reconocen qué otros platos similares pueden cocinar aprovechando lo que ya tienen a mano.

### Perfil de Usuario
> **Martina (24 años):** Cocina para ella y su pareja entre semana. Cuenta con tiempo limitado y busca variar el menú semanal sin necesidad de realizar compras adicionales constantes. Requiere una herramienta simple y rápida que le brinde sugerencias concretas a partir de sus ingredientes o preferencias.

---

## 3. Estado de Avance por Trabajos Prácticos

| TP | Tema Principal | Estado |
| :--- | :--- | :---: |
| **TP0** | Propuesta del Proyecto y Dominio Gastronómico | 🟢 Completado |
| **TP1** | POO, Encapsulamiento y Carga Dinámica desde JSON | 🟢 Completado |
| **TP2** | Análisis de Algoritmos: Búsqueda O(N) vs O(log N) y Benchmarking | 🟢 Completado |
| **TP3** | Árboles Binarios de Búsqueda (ABB) | 🟢 Completado |
| **TP4** | Balanceo de Árboles (AVL) | 🟢 Completado |
| **TP5** | Árboles Generales (N-arios) y Jerarquía de Categorías | 🟢 Completado |
| **TP6** | Heap y Colas de Prioridad (Ranking Top-N) | 🟢 Completado |
| **TP7** | Grafos y Relaciones por Ingredientes | 🟢 Completado |
| **TP8** | Recorridos de Grafos (BFS / DFS) | 🟢 Completado |
| **TP9** | Caminos Mínimos | 🔴 Pendiente |
| **TP10** | Integración y Demo Day | 🔴 Pendiente |

---

## 4. Estructura del Repositorio

```text
SaborBot/
├── algoritmos/             # Algoritmos de ordenamiento, búsqueda y grafos
│   ├── busqueda.py         # Búsqueda secuencial, binaria y exacta (TP3)
│   ├── bfs.py              # Recorrido en Anchura (BFS) y distancias (TP8)
│   ├── caminos.py          # Caminos mínimos (Espacio para TP9)
│   └── dfs.py              # Recorrido en Profundidad (DFS) (TP8)
│   
├── datos/                  # Gestión e ingesta de datos
│   ├── cargador.py         # Módulo de carga y conversión de JSON a objetos Receta
│   └── recetas.json        # Base de datos de prueba
│   
├── docs/                   # Documentación técnica e informes
│   ├── 01-propuesta-dominio.md
│   ├── 02-casos-uso.md
│   ├── 03-diagrama-clases.md
│   ├── 04-diagrama-datos.md
│   ├── 05-gestion-proyecto.md
│   ├── 06-analisis-complejidad.md  # Informe de TP2
│   └── 07_heap_ranking.md          # Informe de TP6
│   
├── estructuras/            # Implementación propia de estructuras de datos
│   ├── arbol.py            # Árbol Binario de Búsqueda (ABB) — TP3
│   ├── arbol_avl.py        # Árbol AVL Auto-balanceado — TP4
│   ├── arbol_n_ario.py     # Árbol General (N-ario) de Categorías — TP5
│   ├── heap.py             # Heap binaria (Max/Min) implementada a mano — TP6
│   └── grafo.py            # Grafo No Dirigido y Pesado (Lista de Adyacencia) — TP7
│   
├── modelos/                # Modelos de dominio (POO)
│   ├── receta.py           # Clase Receta
│   └── usuario.py          # Clase Usuario
│   
├── servicios/              # Lógica de negocio y motor de recomendaciones
│   ├── ranking.py          # Función de prioridad y Top-N con heap — TP6
│   ├── recomendador_grafos.py # Motor de recomendaciones por ingredientes — TP7
│   └── recorridos_grafos.py   # Servicio de consultas BFS y DFS — TP8
│   
├── telegram/               # Integración con Bot de Telegram
│   └── bot.py
│   
├── tests/                  # Pruebas unitarias
│   ├── test_arbol.py       # Tests del ArbolBST (TP3)
│   ├── test_avl.py         # Tests del ArbolAVL (TP4)
│   ├── test_arbol_n_ario.py # Tests del Árbol N-ario (TP5)
│   ├── test_heap.py        # Tests del Heap y del ranking (TP6)
│   ├── test_grafo.py       # Tests del Grafo y recomendaciones (TP7)
│   └── test_recorridos.py  # Tests de BFS y DFS (TP8)
│   
├── ui/                     # Interfaz de usuario
│   └── terminal.py         # Menú interactivo CLI con Dispatch Table (Opciones 1 a 10)
│   
├── experimento.py          # Script de benchmarking (TP2)
├── experimento_arbol.py    # Script de benchmarking: secuencial vs. árbol (TP3)
├── experimento_avl.py      # Script de benchmarking: desbalance BST vs. AVL (TP4)
├── experimento_heap.py     # Script de benchmarking: Top-N con heap vs. ordenar todo (TP6)
├── main.py                 # Punto de entrada de la aplicación
└── README.md               # Documentación principal
```

---

## 5. Resultados del Experimento de Complejidad (TP2)

En el **TP2** evaluamos el rendimiento empírico de la **Búsqueda Secuencial O(N)** frente a la **Búsqueda Binaria O(log N)** utilizando `time.perf_counter()` sobre datasets sintéticos de hasta 100.000 recetas:

- **N = 100:** Busq. Secuencial: 0.0659 ms | Busq. Binaria: 0.0147 ms
- **N = 1.000:** Busq. Secuencial: 0.6138 ms | Busq. Binaria: 0.0240 ms
- **N = 10.000:** Busq. Secuencial: 4.1855 ms | Busq. Binaria: 0.0398 ms
- **N = 100.000:** Busq. Secuencial: 126.0337 ms | Busq. Binaria: 0.0369 ms

**Conclusión del experimento:** Mientras la búsqueda secuencial muestra un crecimiento lineal alcanzando los 126 ms para 100.000 elementos, la búsqueda binaria responde en apenas 0.0369 ms (más de **3.400 veces más rápida**). Esto fundamenta el paso hacia las estructuras de **Árboles Binarios (TP3/TP4)** para mantener las colecciones ordenadas dinámicamente.

---

## 6. Árbol Binario de Búsqueda y Comparación de Estrategias (TP3)

En el **TP3** se incorporó un **Árbol Binario de Búsqueda (ABB)** (`estructuras/arbol.py`), ordenado por el nombre de la receta, integrado a dos funcionalidades reales del menú interactivo:

- **Opción 5 — Buscar receta exacta:** resuelta con `ArbolBST.buscar()`.
- **Opción 6 — Listar alfabéticamente:** resuelta con un recorrido **inorder** del árbol, que entrega las recetas ya ordenadas sin necesidad de un `sort()` adicional.

A diferencia de la búsqueda binaria del TP2 —que exige mantener la lista ordenada, con un costo de reordenamiento O(N log N) ante cada inserción—, el árbol se mantiene ordenado "solo": cada inserción es O(h), sin reordenar el resto de la colección.

### Resultados del experimento (`experimento_arbol.py`)

Comparamos **Búsqueda Secuencial O(N)** vs. **Árbol O(log N)** sobre datasets sintéticos de hasta 50.000 recetas:

- **N = 100:** Secuencial: 0.0163 ms | Árbol: 0.0049 ms | Altura: 16
- **N = 1.000:** Secuencial: 0.0499 ms | Árbol: 0.0048 ms | Altura: 23
- **N = 10.000:** Secuencial: 1.4285 ms | Árbol: 0.0083 ms | Altura: 28
- **N = 50.000:** Secuencial: 12.8376 ms | Árbol: 0.0152 ms | Altura: 37

**Conclusión:** con 500 veces más datos (100 → 50.000), la búsqueda secuencial se volvió ~785 veces más lenta, mientras que el árbol casi no se vio afectado: su altura creció de forma logarítmica (16 → 37), no lineal. Esto confirma en la práctica el análisis teórico O(log n) vs. O(n) — y, a diferencia del TP2, sin pagar el costo de reordenar la colección en cada inserción.

> ⚠️ Este resultado depende de que el árbol no se desbalancee. Insertar los nombres ya ordenados alfabéticamente lo degradaría a una lista enlazada (altura = n). Ese es el problema que resuelve el AVL del TP4.

**Pruebas:** `tests/test_arbol.py` cubre inserción, búsqueda (existente, no existente, case-insensitive, árbol vacío), los tres recorridos (inorder, preorder, postorder), nombres duplicados y altura en casos borde — 11 tests, todos en verde.

---

## 7. Balanceo de Árboles con AVL (TP4)

En el **TP4** investigamos la fragilidad del BST común ante datos en peor caso (por ejemplo, inserción de recetas en orden alfabético estricto). En ese escenario, un BST sin balancear pierde su estructura jerárquica y **degenera en una lista enlazada**, disparando su altura a $h = N$ y convirtiendo la búsqueda en una operación lineal $O(N)$.

Para resolver esta degradación, implementamos un **Árbol AVL (Adelson-Velsky y Landis)** en `estructuras/arbol_avl.py`. La estructura evalúa el **factor de balance** ($h_{izquierda} - h_{derecha}$) de cada nodo y ejecuta auto-balanceo mediante **4 tipos de rotaciones**:

1. **Rotación Simple Derecha** (Desbalance Izquierda - Izquierda)
2. **Rotación Simple Izquierda** (Desbalance Derecha - Derecha)
3. **Doble Rotación Izquierda-Derecha**
4. **Doble Rotación Derecha-Izquierda**

### Resultados del Experimento de Desbalance (`experimento_avl.py`)

Forzamos la inserción de recetas en orden alfabético estricto leyendo desde el cargador de datos `datos/cargador.py`:

- **BST Común (Degenerado):** Altura = $N$ | Complejidad de Búsqueda = $O(N)$ (Comportamiento de Lista).
- **Árbol AVL (Auto-balanceado):** Altura = $h \le 1.44 \log_2 N$ | Complejidad de Búsqueda = $O(\log N)$ garantizado.

**Conclusión Técnica:** Mientras que un BST no balanceado con $10.000$ recetas ordenadas genera una altura de $10.000$ niveles, el **Árbol AVL acorta la altura a solo 14 niveles**, asegurando tiempos de respuesta constantes y eficientes sin importar el orden de ingreso de los datos.

**Pruebas Unitarias:** `tests/test_avl.py` valida las rotaciones automáticas ante inserciones ordenadas, la búsqueda exacta (*case-insensitive*) y el recorrido inorder.

---

## 8. Árboles Generales (N-arios) y Jerarquía de Dominio (TP5)

En el **TP5** incorporamos un **Árbol General (N-ario)** (`estructuras/arbol_n_ario.py`) para representar la jerarquía natural del dominio gastronómico de SaborBot (categorías principales, tipos de platos y subtipos).

### Características Implementadas
- **Nodos N-arios:** Cada nodo almacena un valor de texto y una lista dinámica de hijos (`hijos: List[NodoNArio]`), permitiendo una profundidad ilimitada.
- **Recorridos y Búsqueda:** Implementación propia de búsqueda recursiva de nodos y recorrido en **Preorden**.
- **Visualización en Consola:** Método de impresión estructurado que dibuja las ramas de forma idéntica a un árbol de directorios (*ej. `├── Platos Principales`*).
- **Integración CLI:** Funcionalidad accesible desde el menú interactivo bajo la opción de *"Explorar categorías jerárquicamente"* (`ui/terminal.py`).

**Pruebas Unitarias:** `tests/test_arbol_n_ario.py` valida la correcta búsqueda de nodos existentes/inexistentes y el orden del recorrido preorden.

---

## 9. Heap y Ranking Top-N de Recetas (TP6)

En el **TP6** incorporamos una **Heap binaria** (`estructuras/heap.py`), implementada a mano sobre una lista (sin usar `heapq`), para construir un **ranking dinámico de recetas** (`servicios/ranking.py`). El usuario puede pedir el Top-N general o filtrado por categoría desde el menú interactivo.

### Función de prioridad

No ordenamos solo por valoración: una receta muy bien puntuada pero difícil y larga no es la mejor sugerencia para alguien con poco tiempo, como Martina, nuestra usuaria objetivo. Por eso definimos:

```text
puntaje = valoracion − 0.3 × nivel_dificultad − 0.5 × (tiempo_min / 60)
```

donde `nivel_dificultad` vale 0 (baja), 1 (media) o 2 (alta). Los pesos (`PESO_DIFICULTAD`, `PESO_TIEMPO`) son constantes ajustables en `servicios/ranking.py`.

### Características Implementadas
- **Heap binaria propia:** arreglo donde el padre de la posición `i` es `(i-1)//2` y sus hijos son `2i+1` y `2i+2`. Soporta modo Max y Min mediante una función `clave`.
- **Operaciones:** `insertar`, `extraer`, `ver_raiz`, `reemplazar_raiz` y construcción por *heapify* (`desde_lista`).
- **Top-N con min-heap de tamaño N:** la raíz es la peor de las N mejores recetas vistas hasta el momento; cada receta nueva solo entra al heap si supera a la raíz.
- **Filtro por categoría** y compatibilidad con recetas como objetos o como diccionarios del JSON.
- **Integración CLI:** **Opción 8 — Ver Top-N de recetas (Heap)** en el menú interactivo (`ui/terminal.py`): permite elegir cuántas recetas ver y filtrar por categoría.

### Complejidad

| Operación | Costo |
| :--- | :---: |
| `insertar`, `extraer`, `reemplazar_raiz` | O(log n) |
| `ver_raiz` | O(1) |
| Construcción por heapify (`desde_lista`) | O(n) |
| Top-N con heap de tamaño N sobre m recetas | O(m log N) tiempo, O(N) memoria |
| Top-N ordenando todo | O(m log m) tiempo, O(m) memoria |

### ¿Por qué un heap y no ordenar todo el dataset?
Para un ranking solo interesan las N mejores recetas (N chico, por ejemplo 10) entre m recetas. El heap mantiene únicamente N elementos y evita ordenar las m. Además, permite actualizar el ranking al agregar recetas nuevas sin reordenar toda la colección.

### Resultados del experimento (`experimento_heap.py`)

Comparamos **Top-10 con heap** vs. **ordenar todo con `sorted()` y quedarse con 10** sobre datasets sintéticos:

| N recetas | Heap Top-10 | Ordenar todo |
| :--- | :---: | :---: |
| 1.000 | 0.54 ms | 0.37 ms |
| 10.000 | 4.91 ms | 4.59 ms |
| 100.000 | 47.61 ms | 61.75 ms |

**Conclusión:** con pocos datos, `sorted()` es igual o más rápido porque está implementado en C, mientras que nuestro heap está escrito en Python. A medida que el volumen crece, el heap gana gracias a su complejidad O(m log N) y a su menor uso de memoria. La ventaja del heap es asintótica, no constante.

**Pruebas:** `tests/test_heap.py` cubre extracción en orden, modo min-heap, heapify, heap vacío, `ver_raiz`, el Top-N (orden, N mayor que la cantidad de recetas, filtro por categoría) y la penalización por dificultad — 9 tests, todos en verde.

Más detalle en [`docs/07_heap_ranking.md`](docs/07_heap_ranking.md).

---

## 10. Grafos y Recomendaciones por Ingredientes (TP7)

En el **TP7** incorporamos un **Grafo No Dirigido y Pesado** (`estructuras/grafo.py`) utilizando una **lista de adyacencia** para modelar la red de interconexiones entre las distintas recetas del sistema.

### Diseño y Justificación del Grafo
- **Vértices ($V$):** Cada nodo representa un objeto **Receta** completo de la base de datos.
- **Aristas ($E$):** Dos recetas están conectadas si **comparten al menos un ingrediente** en común.
- **Peso de la arista:** Representa la **cantidad exacta de ingredientes compartidos** entre ambas recetas. Esto permite ponderar la afinidad culinaria.
- **Tipo de grafo:** **No dirigido** (la relación de ingredientes compartidos es simétrica) y **Pesado**.
- **Representación (Lista de adyacencia):** Elegimos un diccionario de diccionarios en Python (`dict[Receta, dict[Receta, int]]`) porque el dominio de SaborBot es un grafo **disperso** (las recetas solo se relacionan con un subconjunto acotado de otras). Esto optimiza drásticamente el uso de memoria $O(V + E)$ en comparación con una matriz de adyacencia estática $O(V^2)$.

### Funcionalidad y Servicio (`servicios/recomendador_grafos.py`)
Se implementó un motor de recomendación que:
1. Construye dinámicamente el grafo cruzando los conjuntos de ingredientes normalizados de todas las recetas.
2. Dada una receta elegida por el usuario, consulta sus vecinos en el grafo y los ordena de mayor a menor afinidad según el peso de la arista (cantidad de ingredientes en común).
3. **Integración CLI:** Accesible desde el menú interactivo bajo la **Opción 9 — Recomendar recetas similares (Grafo)** (`ui/terminal.py`).

**Pruebas Unitarias:** `tests/test_grafo.py` valida la correcta creación de vértices, aristas con pesos, la recuperación de vecinos y las recomendaciones de recetas similares.

---

## 11. Recorridos de Grafos: BFS y DFS (TP8)

En el **TP8** incorporamos los algoritmos fundamentales de exploración sobre la red de recetas de SaborBot, ubicados en la carpeta `algoritmos/`:

### Algoritmos Implementados
- **BFS (Breadth-First Search - `algoritmos/bfs.py`):** 
  - **Qué hace:** Explora el grafo por niveles (en olas), visitando primero a los vecinos directos y luego a los de mayor distancia.
  - **Consulta real en SaborBot:** *"¿Qué recetas están a 1 o 2 saltos de ingredientes?"* (útil para encontrar sustitutos cercanos o variantes directas).
  - **Ventaja:** Garantiza encontrar el camino mínimo en cantidad de aristas.
- **DFS (Depth-First Search - `algoritmos/dfs.py`):**
  - **Qué hace:** Explora un camino tan profundo como sea posible antes de retroceder (*backtracking*).
  - **Consulta real en SaborBot:** *"Explorar la cadena completa de conexiones culinarias en profundidad a partir de una receta base"*.
  - **Ventaja:** Excelente para recorrer toda la componente conexa y analizar la traza profunda de relaciones.

### Análisis de Complejidad
Ambos algoritmos operan con una complejidad temporal de **$O(V + E)$** (donde $V$ es el número de recetas y $E$ la cantidad de conexiones por ingredientes compartidos), ya que cada vértice y arista es visitado a lo más una vez utilizando estructuras auxiliares eficientes (colas para BFS y pilas/recursión para DFS).

**Pruebas Unitarias:** `tests/test_recorridos.py` valida la correcta obtención de distancias por niveles (BFS) y la visita completa de la red (DFS).

---

## 12. Cómo Ejecutar el Proyecto

### Desde el Editor (VS Code / IDE)
1. Abrir el proyecto en tu editor de código.
2. Abrir el archivo ejecutable que desees probar:
   - `main.py` para la aplicación interactiva principal.
   - `experimento.py` para las pruebas de tiempo de Búsqueda Secuencial vs. Binaria (TP2).
   - `experimento_arbol.py` para las pruebas de Búsqueda Secuencial vs. ABB (TP3).
   - `experimento_avl.py` para las pruebas de BST Desbalanceado vs. Árbol AVL (TP4).
   - `experimento_heap.py` para las pruebas de Top-N con Heap vs. ordenar todo (TP6).
3. Ejecutar haciendo clic en el botón de **Play (▶️)** en la esquina superior derecha.

### Desde la Terminal
Parado en la carpeta raíz del proyecto:

```bash
python main.py                                  # aplicación interactiva
python experimento_heap.py                      # benchmark del TP6
python -m unittest discover -s tests -v         # todas las pruebas unitarias
```

---

## 13. Modelo de Usuario (`modelos/usuario.py`)

Para gestionar perfiles y preparar la integración con los algoritmos de recomendación en las siguientes entregas, se implementó el modelo `Usuario` con encapsulamiento estricto y soporte para conjuntos de ingredientes. Contempla la gestión de nombre, email, conjunto de ingredientes disponibles, categorías favoritas e historial de navegación.

---

## 14. Licencia y Uso

Proyecto desarrollado con fines académicos para la materia **Estructuras de Datos** (Universidad Nacional Guillermo Brown).
