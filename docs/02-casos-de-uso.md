# Casos de Uso — SaborBot 

## Actor Principal
- **Usuario:** busca recetas, filtra por ingrediente o categoría, consulta el ranking Top-N, pide recetas similares y explora relaciones mediante recorridos en el grafo.

## Casos de Uso
1. **CU-01 — Buscar receta:** el usuario ingresa un nombre parcial o exacto y obtiene las coincidencias con opción de ver su detalle.
2. **CU-02 — Listar y filtrar recetas:** el usuario visualiza todas las recetas, las ordena alfabéticamente o filtra por categoría o ingrediente.
3. **CU-03 — Explorar categorías:** el usuario navega la estructura jerárquica de categorías gastronómicas.
4. **CU-04 — Consultar Top-N:** el usuario solicita las `N` recetas mejor puntuadas (con filtro opcional por categoría) mediante el servicio de ranking basado en heap.
5. **CU-05 — Recomendar recetas similares:** el usuario elige una receta base y el sistema sugiere platos conectados por ingredientes compartidos, ordenados por cantidad de coincidencias.
6. **CU-06 — Explorar red con BFS y DFS:** el usuario selecciona una receta inicial y consulta recetas cercanas por niveles de distancia en saltos (BFS) o recorre cadenas de conexión en profundidad (DFS).