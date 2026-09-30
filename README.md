# SaborBot — Sistema Inteligente de Recomendación de Recetas

> **Trabajo Práctico Integrador**  
> **Materia:** Estructuras de Datos  
> **Institución:** Universidad Nacional Guillermo Brown (UNAB)  
> **Integrantes:** Jonathan Peralta, Micaela Cafardo  
> **Comisión:** 2 — **Grupo:** 28  
> **Dominio:** Gastronomía  

---

##  1. Descripción General y Dominio

**SaborBot** es un sistema inteligente de recomendación de recetas de cocina desarrollado en Python. Elegimos el dominio de la **gastronomía** porque ofrece relaciones complejas e interconexiones naturales que permiten aplicar de manera progresiva las estructuras de datos fundamentales de la materia:

- **Categorización:** Clasificación de recetas por tipo de plato (*entrada, plato principal, postre*).
- **Relaciones Complejas:** Conexión de recetas mediante ingredientes compartidos, base para el diseño de recomendaciones sobre grafos.
- **Escalabilidad y Rendimiento:** Evaluación empírica de algoritmos a medida que el volumen de datos aumenta.

---

##  2. Problema que Resuelve y Usuario Objetivo

Muchas personas saben qué ingredientes tienen en casa o disfrutan de una receta en particular, pero no reconocen qué otros platillos similares pueden cocinar aprovechando lo que ya tienen a mano.

### Perfil de Usuario
> **Martina (24 años):** Cocina para ella y su pareja entre semana. Cuenta con tiempo limitado y busca variar el menú semanal sin necesidad de realizar compras adicionales constantes. Requiere una herramienta simple y rápida que le brinde sugerencias concretas a partir de sus ingredientes o preferencias.

---

##  3. Estado de Avance por Trabajos Prácticos

| TP | Tema Principal | Estado |
| :--- | :--- | :---: |
| **TP0** | Propuesta del Proyecto y Dominio Gastronómico | 🟢 Completado |
| **TP1** | POO, Encapsulamiento y Carga Dinámica desde JSON | 🟢 Completado |
| **TP2** | Análisis de Algoritmos: Búsqueda O(N) vs O(log N) y Benchmarking | 🟢 Completado |
| **TP3** | Árboles Binarios de Búsqueda (ABB) | 🟢 Completado |
| **TP4** | Balanceo de Árboles (AVL) | 🔴 Pendiente |
| **TP5** | Heaps y Colas de Prioridad (Ranking Top-N) | 🔴 Pendiente |
| **TP6** | Tablas Hash | 🔴 Pendiente |
| **TP7** | Grafos y Recomendaciones Complejas por Ingredientes | 🔴 Pendiente |

---

##  4. Estructura del Repositorio

SaborBot/
├── algoritmos/             # Módulos y estrategias de búsqueda y recorridos
│   ├── bfs.py
│   ├── busqueda.py         # Búsqueda secuencial O(N), binaria O(log N) y secuencial exacta (TP3)
│   ├── caminos.py
│   └── dfs.py
│   
├── datos/                  # Gestión e ingesta de datos
│   ├── cargador.py         # Módulo de carga y conversión de JSON a objetos 
│   └── recetas.json        # Base de datos de prueba
├── docs/                   # Documentación técnica y académica del proyecto
│   ├── capturas/
│   ├── 01-requerimientos.md
│   ├── 02-casos-de-uso.md
│   ├── 03-diagrama-clases.md
│   ├── 04-diagrama-datos.md
│   ├── 05-gestion-proyecto.md
│   └── 06-analisis-complejidad.md  # Informe de TP2
├── estructuras/            # Implementación propia de estructuras de datos
│   ├── arbol.py            # Árbol Binario de Búsqueda (ABB) — implementado en TP3
│   ├── avl.py              # Árbol AVL
│   ├── grafo.py            # Grafo para relaciones entre recetas
│   └── heap.py             # Max/Min Heap para rankings
├── modelos/                # Modelos de dominio (POO)
│   ├── receta.py           # Clase Receta
│   └── usuario.py          # Clase Usuario
├── servicios/              # Lógica de negocio y motor de recomendaciones
│   └── recomendador.py
├── telegram/               # Integración con Bot de Telegram
│   └── bot.py
├── tests/                  # Pruebas unitarias
│   └── test_arbol.py       # 11 tests del ArbolBST (TP3)
├── ui/                     # Interfaz de usuario
│   └── terminal.py         # Menú interactivo CLI con Dispatch Table
├── experimento.py          # Script de benchmarking (TP2)
├── experimento_arbol.py    # Script de benchmarking: secuencial vs. árbol (TP3)
├── main.py                 # Punto de entrada de la aplicación
└── README.md               # Documentación principal

---

##  5. Resultados del Experimento de Complejidad (TP2)

En el **TP2** evaluamos el rendimiento empírico de la **Búsqueda Secuencial O(N)** frente a la **Búsqueda Binaria O(log N)** utilizando `time.perf_counter()` sobre datasets sintéticos de hasta 100.000 recetas:

- **N = 100:** Busq. Secuencial: 0.0659 ms | Busq. Binaria: 0.0147 ms
- **N = 1.000:** Busq. Secuencial: 0.6138 ms | Busq. Binaria: 0.0240 ms
- **N = 10.000:** Busq. Secuencial: 4.1855 ms | Busq. Binaria: 0.0398 ms
- **N = 100.000:** Busq. Secuencial: 126.0337 ms | Busq. Binaria: 0.0369 ms

**Conclusión del experimento:** Mientras la búsqueda secuencial muestra un crecimiento lineal alcanzando los 126 ms para 100.000 elementos, la búsqueda binaria responde en apenas 0.0369 ms (más de **3.400 veces más rápida**). Esto fundamenta el paso hacia las estructuras de **Árboles Binarios (TP3/TP4)** para mantener las colecciones ordenadas dinámicamente.

---

##  6. Árbol Binario de Búsqueda y Comparación de Estrategias (TP3)

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

##  7. Cómo Ejecutar el Proyecto

### Desde el Editor (VS Code / IDE)
1. Abrir el proyecto en tu editor.
2. Abrir el archivo `main.py` para la aplicación principal, `experimento.py` para las pruebas de tiempo del TP2, o `experimento_arbol.py` para las del TP3.
3. Ejecutar haciendo clic en el botón de **Play (▶️)** en la esquina superior derecha.

### Desde la Consola
- **Menú Interactivo:** `python main.py`
- **Benchmarking TP2:** `python experimento.py`
- **Benchmarking TP3 (árbol):** `python experimento_arbol.py`
- **Tests del árbol:** `python -m unittest tests.test_arbol -v`

---

##  8. Modelo de Usuario (modelos/usuario.py)

Para gestionar perfiles y preparar la integración con los algoritmos de recomendación en las siguientes entregas, se implementó el modelo `Usuario` con encapsulamiento estricto y soporte para conjuntos de ingredientes. Contempla la gestión de nombre, email, conjunto de ingredientes disponibles, categorías favoritas e historial de navegación.

---

##  9. Licencia y Uso
Proyecto desarrollado con fines académicos para la materia **Estructuras de Datos** (Universidad Nacional Guillermo Brown).
