"""
TP3 — Árbol Binario de Búsqueda (ABB / BST) de recetas.

Clave de ordenamiento: el NOMBRE de la receta (en minúscula).

¿Por qué el nombre y no el rating o el año?
--------------------------------------------
La operación crítica del sistema (ver docs/06-analisis-complejidad.md,
TP2) es "buscar receta por nombre". En TP2 ya vimos que la búsqueda
binaria gana a la secuencial, pero exige mantener la lista ordenada
(costo O(N log N) si se reordena tras cada inserción). El ABB resuelve
el mismo problema sin pagar ese costo de reordenamiento: cada inserción
es O(h), y el árbol queda ordenado "solo", listo para recorrerse en
cualquier momento con un inorder.

El ranking por valoración (rating) no usa esta clave: se va a resolver
con un heap (TP futuro), pensado específicamente para Top-N.

Búsqueda EXACTA vs. PARCIAL:
-----------------------------
Este árbol resuelve búsqueda EXACTA por nombre (útil para revisar el
detalle de una receta puntual). La búsqueda PARCIAL ("contiene la
palabra X") sigue resolviéndose con buscar_por_nombre (secuencial),
porque un árbol ordenado alfabéticamente no acelera ese tipo de consulta:
la coincidencia parcial puede estar en cualquier rama.
"""


class NodoArbol:
    def __init__(self, receta):
        self.receta = receta
        self.izquierda = None
        self.derecha = None

    @property
    def clave(self):
        return self.receta.nombre.lower()


class ArbolBST:
    def __init__(self):
        self._raiz = None
        self._cantidad = 0

    def __len__(self):
        return self._cantidad

    # ---------------- Inserción ----------------
    def insertar(self, receta):
        """Complejidad: O(h), h = altura del árbol.
        Caso promedio (inserción en orden razonablemente aleatorio): O(log n).
        Peor caso (árbol degenerado): O(n).
        """
        nodo_nuevo = NodoArbol(receta)
        self._cantidad += 1

        if self._raiz is None:
            self._raiz = nodo_nuevo
            return

        actual = self._raiz
        while True:
            if nodo_nuevo.clave < actual.clave:
                if actual.izquierda is None:
                    actual.izquierda = nodo_nuevo
                    return
                actual = actual.izquierda
            elif nodo_nuevo.clave > actual.clave:
                if actual.derecha is None:
                    actual.derecha = nodo_nuevo
                    return
                actual = actual.derecha
            else:
                actual.receta = nodo_nuevo.receta  # nombre duplicado: reemplaza
                self._cantidad -= 1
                return

    # ---------------- Búsqueda ----------------
    def buscar(self, nombre):
        """Búsqueda EXACTA (case-insensitive) por nombre.
        Complejidad: O(h) -> O(log n) en el caso promedio, O(n) en el peor caso.
        Se compara contra buscar_exacta_secuencial (algoritmos/busqueda.py)
        en experimento_arbol.py.
        """
        clave = nombre.strip().lower()
        actual = self._raiz
        while actual is not None:
            if clave == actual.clave:
                return actual.receta
            elif clave < actual.clave:
                actual = actual.izquierda
            else:
                actual = actual.derecha
        return None

    # ---------------- Recorridos ----------------
    def inorder(self):
        """izq, raíz, der -> recetas ordenadas alfabéticamente."""
        resultado = []
        self._inorder(self._raiz, resultado)
        return resultado

    def _inorder(self, nodo, resultado):
        if nodo is None:
            return
        self._inorder(nodo.izquierda, resultado)
        resultado.append(nodo.receta)
        self._inorder(nodo.derecha, resultado)

    def preorder(self):
        """raíz, izq, der -> útil para reconstruir/exportar el árbol."""
        resultado = []
        self._preorder(self._raiz, resultado)
        return resultado

    def _preorder(self, nodo, resultado):
        if nodo is None:
            return
        resultado.append(nodo.receta)
        self._preorder(nodo.izquierda, resultado)
        self._preorder(nodo.derecha, resultado)

    def postorder(self):
        """izq, der, raíz -> útil para eliminar el árbol de abajo hacia arriba."""
        resultado = []
        self._postorder(self._raiz, resultado)
        return resultado

    def _postorder(self, nodo, resultado):
        if nodo is None:
            return
        self._postorder(nodo.izquierda, resultado)
        self._postorder(nodo.derecha, resultado)
        resultado.append(nodo.receta)

    # ---------------- Utilidades ----------------
    def altura(self):
        """Iterativa a propósito: un árbol degenerado (nombres insertados ya
        ordenados) puede tener altura = n, y una versión recursiva agotaría
        la pila de Python con datasets grandes."""
        if self._raiz is None:
            return 0
        altura_max = 0
        pila = [(self._raiz, 1)]
        while pila:
            nodo, profundidad = pila.pop()
            altura_max = max(altura_max, profundidad)
            if nodo.izquierda:
                pila.append((nodo.izquierda, profundidad + 1))
            if nodo.derecha:
                pila.append((nodo.derecha, profundidad + 1))
        return altura_max

    @classmethod
    def construir_desde(cls, recetas):
        arbol = cls()
        for r in recetas:
            arbol.insertar(r)
        return arbol
