from typing import Optional, List
from modelos.receta import Receta


class NodoAVL:
    """Nodo para el Árbol AVL con cálculo implícito de altura."""
    def __init__(self, receta: Receta):
        self.receta: Receta = receta
        self.clave: str = receta.nombre.strip().lower()
        self.izquierda: Optional['NodoAVL'] = None
        self.derecha: Optional['NodoAVL'] = None
        self.altura: int = 1


class ArbolAVL:
    """
    Árbol Binario de Búsqueda Auto-Balanceado (AVL) - TP4.
    Garantiza una altura h = O(log N) incluso ante inserciones en orden alfabético.
    """
    def __init__(self):
        self.raiz: Optional[NodoAVL] = None
        self._cantidad: int = 0

    def __len__(self) -> int:
        return self._cantidad

    def _obtener_altura(self, nodo: Optional[NodoAVL]) -> int:
        return nodo.altura if nodo else 0

    def _factor_balance(self, nodo: Optional[NodoAVL]) -> int:
        return self._obtener_altura(nodo.izquierda) - self._obtener_altura(nodo.derecha) if nodo else 0

    def _actualizar_altura(self, nodo: NodoAVL) -> None:
        nodo.altura = 1 + max(self._obtener_altura(nodo.izquierda), self._obtener_altura(nodo.derecha))

    # --- ROTACIONES DE BALANCEO ---
    def _rotacion_derecha(self, y: NodoAVL) -> NodoAVL:
        x = y.izquierda
        T2 = x.derecha

        # Ejecutar rotación
        x.derecha = y
        y.izquierda = T2

        # Actualizar alturas
        self._actualizar_altura(y)
        self._actualizar_altura(x)

        return x

    def _rotacion_izquierda(self, x: NodoAVL) -> NodoAVL:
        y = x.derecha
        T2 = y.izquierda

        # Ejecutar rotación
        y.izquierda = x
        x.derecha = T2

        # Actualizar alturas
        self._actualizar_altura(x)
        self._actualizar_altura(y)

        return y

    # --- INSERCIÓN Y AUTO-BALANCEO ---
    def insertar(self, receta: Receta) -> None:
        """Inserta una receta y rebalancea el árbol automáticamente en O(log N)."""
        self.raiz = self._insertar_recursivo(self.raiz, receta)

    def _insertar_recursivo(self, nodo: Optional[NodoAVL], receta: Receta) -> NodoAVL:
        clave_nueva = receta.nombre.strip().lower()

        # 1. Inserción estándar de BST
        if nodo is None:
            self._cantidad += 1
            return NodoAVL(receta)

        if clave_nueva < nodo.clave:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, receta)
        elif clave_nueva > nodo.clave:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, receta)
        else:
            nodo.receta = receta  # Reemplaza si la clave ya existe
            return nodo

        # 2. Actualizar altura
        self._actualizar_altura(nodo)

        # 3. Obtener el factor de balance
        balance = self._factor_balance(nodo)

        # 4. Aplicar rotaciones si hay desbalance
        # Caso Izquierda - Izquierda
        if balance > 1 and clave_nueva < nodo.izquierda.clave:
            return self._rotacion_derecha(nodo)

        # Caso Derecha - Derecha
        if balance < -1 and clave_nueva > nodo.derecha.clave:
            return self._rotacion_izquierda(nodo)

        # Caso Izquierda - Derecha
        if balance > 1 and clave_nueva > nodo.izquierda.clave:
            nodo.izquierda = self._rotacion_izquierda(nodo.izquierda)
            return self._rotacion_derecha(nodo)

        # Caso Derecha - Izquierda
        if balance < -1 and clave_nueva < nodo.derecha.clave:
            nodo.derecha = self._rotacion_derecha(nodo.derecha)
            return self._rotacion_izquierda(nodo)

        return nodo

    # --- BÚSQUEDA ---
    def buscar(self, nombre: str) -> Optional[Receta]:
        """Búsqueda exacta por nombre en O(log N) garantizado."""
        clave = nombre.strip().lower()
        actual = self.raiz
        while actual:
            if clave == actual.clave:
                return actual.receta
            elif clave < actual.clave:
                actual = actual.izquierda
            else:
                actual = actual.derecha
        return None

    # --- RECORRIDO INORDER ---
    def inorder(self) -> List[Receta]:
        """Devuelve las recetas en orden alfabético A-Z."""
        resultado = []
        self._inorder(self.raiz, resultado)
        return resultado

    def _inorder(self, nodo: Optional[NodoAVL], resultado: List[Receta]) -> None:
        if nodo:
            self._inorder(nodo.izquierda, resultado)
            resultado.append(nodo.receta)
            self._inorder(nodo.derecha, resultado)

    def altura(self) -> int:
        return self._obtener_altura(self.raiz)

    @classmethod
    def construir_desde(cls, recetas: List[Receta]) -> 'ArbolAVL':
        arbol = cls()
        for r in recetas:
            arbol.insertar(r)
        return arbol