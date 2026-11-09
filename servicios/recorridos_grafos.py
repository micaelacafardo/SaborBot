"""Servicio de consultas reales mediante recorridos BFS y DFS (TP8)."""
from algoritmos.bfs import bfs
from algoritmos.dfs import dfs

def explorar_cercanas_bfs(receta_inicio, grafo, nivel_max=2):
    """Consulta BFS: Devuelve las recetas agrupadas por nivel de cercanía (distancia en aristas).
    Útil para encontrar sustitutos inmediatos o recetas a 1 o 2 saltos de ingredientes.
    """
    _, distancias = bfs(grafo, receta_inicio)
    
    por_nivel = {}
    for receta, dist in distancias.items():
        if 0 < dist <= nivel_max:
            if dist not in por_nivel:
                por_nivel[dist] = []
            por_nivel[dist].append(receta)
            
    return por_nivel

def explorar_cadena_dfs(receta_inicio, grafo):
    """Consulta DFS: Explora en profundidad toda la cadena de relaciones a partir de la receta base."""
    return dfs(grafo, receta_inicio)