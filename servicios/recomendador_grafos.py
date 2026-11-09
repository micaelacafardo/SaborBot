from estructuras.grafo import Grafo

def construir_grafo_recetas(recetas):
    """Construye un grafo no dirigido y pesado donde:
    - Vértices: Objetos Receta.
    - Aristas: Conexión si comparten al menos un ingrediente.
    - Peso: Cantidad de ingredientes compartidos.
    """
    grafo = Grafo()
    
    # Normalizar ingredientes de cada receta para comparar correctamente
    recetas_ingredientes = {}
    for r in recetas:
        grafo.agregar_vertice(r)
        ingrs = set(ing.lower().strip() for ing in getattr(r, 'ingredientes', []))
        recetas_ingredientes[r] = ingrs

    # Conectar pares de recetas que compartan ingredientes
    lista_recetas = list(recetas)
    n = len(lista_recetas)
    for i in range(n):
        for j in range(i + 1, n):
            r1 = lista_recetas[i]
            r2 = lista_recetas[j]
            
            compartidos = recetas_ingredientes[r1].intersection(recetas_ingredientes[r2])
            if compartidos:
                peso = len(compartidos)
                grafo.agregar_arista(r1, r2, peso=peso)
                
    return grafo

def recomendar_similares(receta_objetivo, grafo, top_n=5):
    """Recomienda recetas similares a una dada basándose en los vecinos del grafo,
    ordenados de mayor a menor peso (cantidad de ingredientes compartidos).
    """
    vecinos = grafo.obtener_vecinos(receta_objetivo)
    if not vecinos:
        return []
    
    # Ordenamos a los vecinos por peso descendente (más ingredientes en común primero)
    vecinos_ordenados = sorted(vecinos.items(), key=lambda x: x[1], reverse=True)
    
    return [(vecina, peso) for vecina, peso in vecinos_ordenados[:top_n]]