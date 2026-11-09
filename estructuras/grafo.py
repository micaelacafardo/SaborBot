class Grafo:
    def __init__(self):
        # Diccionario de adyacencia: { vertice: { vecino: peso, ... }, ... }
        self._adyacencias = {}

    def agregar_vertice(self, vertice):
        """Agrega un vértice al grafo si no existe."""
        if vertice not in self._adyacencias:
            self._adyacencias[vertice] = {}

    def agregar_arista(self, origen, destino, peso=1):
        """Agrega una arista no dirigida entre origen y destino con su respectivo peso."""
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        # Al ser un grafo no dirigido, la conexión es bidireccional
        self._adyacencias[origen][destino] = peso
        self._adyacencias[destino][origen] = peso

    def obtener_vecinos(self, vertice):
        """Devuelve un diccionario con los vecinos y el peso de sus aristas."""
        if vertice in self._adyacencias:
            return self._adyacencias[vertice]
        return {}

    def obtener_vertices(self):
        """Devuelve una lista con todos los vértices (nodos) del grafo."""
        return list(self._adyacencias.keys())

    def existe_vertice(self, vertice):
        """Verifica si un vértice pertenece al grafo."""
        return vertice in self._adyacencias

    def __len__(self):
        """Devuelve la cantidad total de vértices."""
        return len(self._adyacencias)