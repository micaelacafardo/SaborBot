# 05 - Gestión de Proyecto: Trello y Scrum

## 1. Enlace al Tablero de Gestión
El seguimiento del proyecto y la asignación de tareas se lleva a cabo mediante el siguiente tablero:
- **Tablero Trello:** [Ver Tablero de SaborBot](https://trello.com/b/7ynYhQKG/saborbot)

## 2. Estructura del Tablero
El tablero cuenta con las cuatro columnas mínimas de seguimiento:
1. **Backlog:** Tareas futuras y requerimientos planificados para próximos Sprints (TP2, TP3, TP7).
2. **En progreso:** Tareas actualmente en desarrollo durante el Sprint activo.
3. **En revisión:** Funcionalidades terminadas pendientes de pruebas o revisión de código entre los integrantes.
4. **Hecho:** Tareas completamente finalizadas y validadas.

---

## 3. Metodología de Trabajo (Scrum Simplificado)
Para la organización de la cursada adoptamos un esquema de **Scrum simplificado**:

* **Sprints:** Definimos **1 Sprint por cada Trabajo Práctico**. Cada Sprint abarca el ciclo de desarrollo desde la lectura de la consigna hasta la entrega funcional.
* **Historias de Usuario:** Los requerimientos del sistema se definen desde la perspectiva del usuario con criterios de aceptación claros e independientes.
* **Retrospectiva Breve:** Al finalizar la entrega de cada TP, realizamos una puesta en común para analizar:
  1. ¿Qué funcionó bien durante el Sprint?
  2. ¿Qué dificultades o trabas tuvimos?
  3. ¿Qué ajustes realizaremos para el próximo Sprint?

---

## 4. Historia de Usuario y Criterios de Aceptación (Ejemplo)

### Historia de Usuario 1: Búsqueda parcial de recetas
> **Como usuario de SaborBot**, quiero buscar recetas ingresando una palabra o término clave para encontrar rápidamente ideas de cocina sin recordar el nombre exacto.

**Criterios de aceptación:**
* La búsqueda permite coincidencias parciales (ejemplo: buscar "mila" retorna "Milanesa con puré" y "Milanesa napolitana").
* La búsqueda es insensible a mayúsculas y minúsculas (*case-insensitive*).
* Si existen coincidencias, el sistema devuelve un listado ordenado; si no se encuentran resultados, emite un mensaje indicando que no hay coincidencias.

---

### Historia de Usuario 2: Comparación por ingredientes
> **Como usuario**, quiero ver si una receta comparte ingredientes con otra para aprovechar insumos disponibles en mi cocina.

**Criterios de aceptación:**
* El método compara los conjuntos de ingredientes de ambas recetas.
* Retorna únicamente la intersección de ingredientes compartidos.