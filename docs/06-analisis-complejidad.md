# Informe de Análisis de Complejidad y Benchmarking (TP2)

---

## 1. Introducción Teórica

El objetivo de este análisis es evaluar  el rendimiento de dos estrategias de búsqueda fundamentales sobre el conjunto de datos de recetas de **SaborBot**:

1. **Búsqueda Secuencial (Lineal):** Recorre la lista elemento por elemento comprobando coincidencias.
2. **Búsqueda Binaria:** Requiere un conjunto previamente ordenado por la clave de búsqueda (nombre) y divide el espacio de búsqueda a la mitad en cada iteración.

---

## 2. Análisis Formal de Notación Big-$O$

### A. Búsqueda Secuencial
- **Peor Caso $O(N)$:** El elemento buscado no existe o está en la última posición de la lista. Requiere $N$ comparaciones.
- **Caso Promedio $O(N)$:** En promedio, se inspeccionan $N/2$ elementos, lo que asintóticamente equivale a $O(N)$.
- **Mejor Caso $O(1)$:** El elemento buscado se encuentra en la primera posición.

### B. Búsqueda Binaria
- **Peor Caso $O(\log N)$:** Se reduce el espacio de búsqueda dividiéndolo por 2 en cada paso hasta alcanzar una lista de tamaño 1. El número máximo de comparaciones es $\lfloor \log_2 N \rfloor + 1$.
- **Caso Promedio $O(\log N)$:** La mayoría de los elementos requieren una cantidad logarítmica de divisiones.
- **Mejor Caso $O(1)$:** El elemento buscado coincide exactamente con el elemento del medio en la primera iteración.

---

## 3. Resultados Empíricos (Benchmark)

El experimento se ejecutó utilizando la librería nativa `time.perf_counter()` sobre datasets sintéticos escalados desde $100$ hasta $100.000$ recetas.

### Tabla Comparativa de Tiempos Ejecutados

| N Recetas | Búsqueda Secuencial $O(N)$ | Búsqueda Binaria $O(\log N)$ | Factor de Eficiencia |
| :--- | :--- | :--- | :--- |
| **100** | $0.0659\text{ ms}$ | $0.0147\text{ ms}$ | **4.48x más rápida** |
| **1.000** | $0.6138\text{ ms}$ | $0.0240\text{ ms}$ | **25.57x más rápida** |
| **10.000** | $4.1855\text{ ms}$ | $0.0398\text{ ms}$ | **105.16x más rápida** |
| **100.000** | $126.0337\text{ ms}$ | $0.0369\text{ ms}$ | **3.415,54x más rápida** |

---

## 4. Conclusiones

1. **Escalabilidad Lineal vs. Logarítmica:** Para volúmenes pequeños ($N=100$), la diferencia en milisegundos es imperceptible para el usuario. Sin embargo, al escalar a $N=100.000$, la Búsqueda Secuencial tarda más de $126\text{ ms}$, mientras que la Binaria resuelve en tan solo $0.0369\text{ ms}$.
2. **Costo Previo de Ordenamiento:** La Búsqueda Binaria exige que la lista esté ordenada ($O(N \log N)$ para ordenar). Por lo tanto, se justifica cuando se realizan múltiples búsquedas sobre un conjunto estático o poco cambiante.
3. **Justificación para TP3 (Árboles):** Para mantener una estructura dinámicamente ordenada con inserciones, búsquedas y eliminaciones eficientes sin pagar el costo de reordenar un arreglo, la transición natural es migrar hacia **Árboles Binarios de Búsqueda (ABB)** y **Árboles AVL**.
