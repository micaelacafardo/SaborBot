"""Algoritmo de Recorrido en Anchura (BFS) sobre Grafos (TP8)."""
from collections import deque

def bfs(grafo, inicio):
    """Realiza un recorrido en Anchura (BFS) desde el vértice inicial.
    
    Explora el grafo por niveles (en olas), garantizando la menor distancia 
    en cantidad de aristas desde el origen.
    
    Retorna:
    - orden_visitados: Lista de vértices en el orden en que fueron descubiertos.
    - distancias: Diccionario {vertice: cantidad_de_saltos_desde_inicio}.
    
    Complejidad: O(V + E)
    """
    if not grafo.existe_vertice(inicio):
        return [], {}

    visitados = set([inicio])
    cola = deque([inicio])
    orden_visitados = []
    distancias = {inicio: 0}

    while cola:
        vertice = cola.popleft()
        orden_visitados.append(vertice)

        for vecino in grafo.obtener_vecinos(vertice):
            if vecino not in visitados:
                visitados.add(vecino)
                distancias[vecino] = distancias[vertice] + 1
                cola.append(vecino)

    return orden_visitados, distancias