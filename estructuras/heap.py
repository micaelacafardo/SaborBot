"""Heap binaria implementada a mano (TP6).

Se guarda en una lista; para el nodo en la posición i:
    padre  = (i - 1) // 2
    hijo izq = 2*i + 1
    hijo der = 2*i + 2

Por defecto es un MAX-heap (la raíz es el elemento de mayor prioridad).
La prioridad de cada elemento la calcula la función `clave`.
"""


class Heap:
    def __init__(self, clave=lambda x: x, max_heap=True):
        self._datos = []
        self._clave = clave
        self._max = max_heap

    # ---------- utilidades ----------
    def __len__(self):
        return len(self._datos)

    def esta_vacio(self):
        return len(self._datos) == 0

    def ver_raiz(self):
        """Devuelve el elemento de mayor prioridad sin sacarlo. O(1)."""
        if self.esta_vacio():
            raise IndexError("el heap está vacío")
        return self._datos[0]

    def _antes(self, a, b):
        """True si 'a' debe estar más arriba que 'b' en el heap."""
        ka, kb = self._clave(a), self._clave(b)
        return ka > kb if self._max else ka < kb

    def _intercambiar(self, i, j):
        self._datos[i], self._datos[j] = self._datos[j], self._datos[i]

    # ---------- operaciones ----------
    def insertar(self, elemento):
        """Agrega al final y lo 'sube' hasta su lugar. O(log n)."""
        self._datos.append(elemento)
        self._subir(len(self._datos) - 1)

    def extraer(self):
        """Saca y devuelve la raíz. O(log n)."""
        if self.esta_vacio():
            raise IndexError("el heap está vacío")
        self._intercambiar(0, len(self._datos) - 1)
        raiz = self._datos.pop()
        if self._datos:
            self._bajar(0)
        return raiz

    def reemplazar_raiz(self, elemento):
        """Reemplaza la raíz por otro elemento y reacomoda. O(log n)."""
        if self.esta_vacio():
            raise IndexError("el heap está vacío")
        raiz = self._datos[0]
        self._datos[0] = elemento
        self._bajar(0)
        return raiz

    @classmethod
    def desde_lista(cls, elementos, clave=lambda x: x, max_heap=True):
        """Construye el heap de una vez (heapify). O(n), mejor que n inserciones."""
        h = cls(clave, max_heap)
        h._datos = list(elementos)
        for i in range(len(h._datos) // 2 - 1, -1, -1):
            h._bajar(i)
        return h

    # ---------- internas ----------
    def _subir(self, i):
        while i > 0:
            padre = (i - 1) // 2
            if self._antes(self._datos[i], self._datos[padre]):
                self._intercambiar(i, padre)
                i = padre
            else:
                break

    def _bajar(self, i):
        n = len(self._datos)
        while True:
            izq, der = 2 * i + 1, 2 * i + 2
            mejor = i
            if izq < n and self._antes(self._datos[izq], self._datos[mejor]):
                mejor = izq
            if der < n and self._antes(self._datos[der], self._datos[mejor]):
                mejor = der
            if mejor == i:
                break
            self._intercambiar(i, mejor)
            i = mejor