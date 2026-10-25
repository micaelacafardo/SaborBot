from typing import List, Optional

class NodoNArio:
    """Nodo para un Árbol General (N-ario) con múltiples hijos."""
    def __init__(self, valor: str):
        self.valor: str = valor
        self.hijos: List['NodoNArio'] = []

    def agregar_hijo(self, hijo: 'NodoNArio') -> 'NodoNArio':
        self.hijos.append(hijo)
        return hijo


class ArbolNArio:
    """Árbol General (N-ario) para representar jerarquías del dominio gastronómico."""
    def __init__(self, raiz_valor: str):
        self.raiz: NodoNArio = NodoNArio(raiz_valor)

    def buscar(self, valor: str) -> Optional[NodoNArio]:
        """Busca un nodo por su valor de manera recursiva en el árbol N-ario."""
        return self._buscar_recursivo(self.raiz, valor.strip().lower())

    def _buscar_recursivo(self, nodo: NodoNArio, valor_buscado: str) -> Optional[NodoNArio]:
        if nodo.valor.strip().lower() == valor_buscado:
            return nodo
        for hijo in nodo.hijos:
            encontrado = self._buscar_recursivo(hijo, valor_buscado)
            if encontrado:
                return encontrado
        return None

    def recorrer_preorden(self) -> List[str]:
        """Devuelve un recorrido en preorden de todos los valores del árbol."""
        resultado = []
        self._preorden_recursivo(self.raiz, resultado)
        return resultado

    def _preorden_recursivo(self, nodo: NodoNArio, resultado: List[str]):
        if nodo:
            resultado.append(nodo.valor)
            for hijo in nodo.hijos:
                self._preorden_recursivo(hijo, resultado)

    def imprimir_jerarquia(self, nodo: Optional[NodoNArio] = None, nivel: int = 0):
        """Muestra la jerarquía visualmente en la terminal con formato de árbol."""
        if nodo is None:
            nodo = self.raiz
        
        prefijo = "│   " * (nivel - 1) + "├── " if nivel > 0 else ""
        print(f"{prefijo}{nodo.valor}")
        
        for hijo in nodo.hijos:
            self.imprimir_jerarquia(hijo, nivel + 1)