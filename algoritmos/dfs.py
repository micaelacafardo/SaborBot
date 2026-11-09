"""Algoritmo de Recorrido en Profundidad (DFS) sobre Grafos (TP8)."""

def dfs(grafo, inicio):
    """Realiza un recorrido DFS desde el vértice inicial.
    
    Retorna la lista de vértices visitados en orden de exploración.
    Complejidad: O(V + E)
    """
    if not grafo.existe_vertice(inicio):
        return []

    visitados = set()
    orden_visitados = []

    def _dfs_recursivo(v):
        visitados.add(v)
        orden_visitados.append(v)
        for vecino in grafo.obtener_vecinos(v):
            if vecino not in visitados:
                _dfs_recursivo(vecino)

    _dfs_recursivo(inicio)
    return orden_visitados