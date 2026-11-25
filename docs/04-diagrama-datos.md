# Diagrama de Datos — SaborBot 

## 1. Origen de los Datos (`datos/recetas.json`)
El sistema carga las recetas desde `datos/recetas.json` a través de `datos/cargador.py`. Cada registro aporta:
- **Atributos descriptivos:** `nombre`, `categoria`, `dificultad`.
- **Métrica de calidad:** `valoracion`.
- **Lista de ingredientes:** colección de textos que luego se normalizan (minúsculas, sin espacios extra) para comparar afinidad culinaria.

## 2. Estructuras en Memoria y Relaciones
- **Colección base (`list[Receta]`):** mantiene todas las recetas cargadas para listados, filtros y construcción de estructuras.
- **Estructuras arbóreas y heap:** organizan las recetas o sus claves/prioridades según la operación (`ArbolBST`, `ArbolAVL`, `ArbolNario`, `Heap`).
- **Grafo en memoria (`dict[Receta, dict[Receta, int]]`):**
  - Cada **vértice** es un objeto `Receta`.
  - Cada **arista no dirigida** vincula dos recetas que comparten al menos un ingrediente normalizado.
  - El **peso** (`int`) indica cuántos ingredientes tienen en común.

## 3. Diagrama Entidad-Relación (Mermaid)

```mermaid
erDiagram
    RECETA {
        string nombre
        string categoria
        string dificultad
        float valoracion
    }
    INGREDIENTE {
        string nombre_normalizado
    }
    CONEXION_RECETA {
        int peso_ingredientes_compartidos
    }

    RECETA ||--|{ INGREDIENTE : contiene
    RECETA ||--o{ CONEXION_RECETA : conecta_con