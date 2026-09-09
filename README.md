#  SaborBot — Sistema de Recomendaciones Gastronómicas

> **Trabajo Práctico Integrador**  
> <br>
> **Materia:** Estructuras de Datos  
> <br>
> **Integrantes:** Jonathan Peralta, Micaela Cafardo  
> <br>
> **Dominio:** Gastronomía  

---

##  1. Nombre del Proyecto
**SaborBot**

---

##  2. Dominio Elegido y Justificación

Elegimos la **gastronomía (recetas de cocina)** porque es un dominio con relaciones ricas para modelar a lo largo de toda la cursada:

- **Categorización:** Las recetas se agrupan por tipo de plato (*entrada, plato principal, postre*) y por tipo de cocina (*italiana, mexicana, casera*).
- **Relaciones complejas:** Se pueden conectar entre sí a través de los **ingredientes que comparten**, lo que resulta ideal para construir un **grafo** en las etapas de recorridos y caminos mínimos.
- **Familiaridad:** Es un dominio cercano a todos los integrantes del equipo, lo que facilita la carga de datos reales y de calidad.

---

##  3. Problema que Resuelve

Muchas veces sabemos qué ingredientes tenemos disponibles o nos gustó una receta puntual, pero no sabemos qué otra cosa cocinar que sea parecida o que aproveche lo que ya tenemos. 

**SaborBot** resuelve este problema permitiendo:
1. Buscar y ordenar recetas por valoración.
2. Explorar platos por categoría.
3. Recomendar recetas relacionadas a partir de una que ya le haya gustado al usuario.

---

##  4. Usuario Objetivo


> **Martina (24 años)**  
> Cocina para ella y su pareja entre semana. Tiene poco tiempo disponible y quiere variar el menú sin tener que salir a comprar ingredientes nuevos todo el tiempo. Busca una herramienta simple y rápida que le sugiera qué cocinar a partir de lo que ya conoce o tiene a mano.

---

##  5. Cinco Funcionalidades Iniciales

| # | Funcionalidad | Descripción |
| :-: | :--- | :--- |
| **1** | **Buscar receta** | Permite buscar por nombre o por ingrediente principal. |
| **2** | **Ver Top 10** | Muestra las 10 recetas mejor valoradas. |
| **3** | **Explorar categorías** | Navega por *entrada*, *plato principal*, *postre*, etc. |
| **4** | **Ver recetas relacionadas** | Muestra recetas que comparten ingredientes con una dada. |
| **5** | **Obtener recomendación** | Sugiere una nueva receta a partir de una que le gustó al usuario. |

---

## 6. Ejemplo de Interacción

**Comandos del usuario:**

```text
> Buscar receta: "Milanesa con puré"
> Recetas relacionadas con Milanesa con puré
> ¿Qué puedo cocinar si me gustó la Milanesa con puré?
> Top 10 recetas mejor valoradas
```

**Salida esperada:**

```text
SABORBOT
----------------------------------------
Si te gustó MILANESA CON PURÉ,
quizás te interesen:

1. Milanesa napolitana      - 9.0
2. Puré rústico              - 8.7
3. Escalope con papas        - 8.5
```

---

##  7. Boceto de la Interfaz de Terminal

```text
========================================
          SABORBOT — TERMINAL
========================================

1. Buscar receta
2. Explorar categorías
3. Ver Top 10
4. Ver recetas relacionadas
5. Explorar conexiones
6. Encontrar camino entre recetas
7. Obtener recomendaciones
0. Salir

----------------------------------------
Opción:
```

---

##  8. Boceto Inicial de Clases y Componentes

```python
class Receta:
    nombre: str
    categoria: str
    ingredientes: list[str]
    dificultad: str
    valoracion: float
```

**Estructura general:**

```text
Recomendador
  ├── usa ➔ ArbolBST<Receta>   (búsqueda por nombre)
  ├── usa ➔ Heap<Receta>       (ranking Top-N por valoración)
  └── usa ➔ Grafo<Receta>      (relaciones por ingredientes compartidos)
```

> [!IMPORTANT]
> Este diagrama es un primer boceto: se irá ampliando en el **TP1** *(clases y encapsulamiento)* y en el **TP7** *(definición formal del grafo: vértices, aristas y tipo de grafo)*.

---

> *Entregable TP0 — Versión inicial sujeta a ajustes en próximas etapas.*