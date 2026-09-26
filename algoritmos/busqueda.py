# ==============================================================================
# ESTRATEGIA A: Búsqueda Secuencial (O(N)) - TP1
# ==============================================================================
def buscar_por_nombre(recetas, termino):
    """
    Recorre la lista elemento por elemento (O(N)).
    Permite coincidencia parcial.
    """
    termino = termino.strip().lower()
    resultados = []
    for receta in recetas:
        if termino in receta.nombre.lower():
            resultados.append(receta)
    return resultados


# ==============================================================================
# ESTRATEGIA B: Búsqueda Binaria (O(log N)) - TP2
# ==============================================================================
def busqueda_binaria_por_nombre(recetas_ordenadas, nombre_exacto):
    """
    Busca dividiendo a la mitad en cada paso (O(log N)).
    IMPORTANTE: Requiere que 'recetas_ordenadas' esté ordenada alfabéticamente por nombre.
    """
    inicio = 0
    fin = len(recetas_ordenadas) - 1
    nombre_exacto = nombre_exacto.strip().lower()

    while inicio <= fin:
        medio = (inicio + fin) // 2
        nombre_actual = recetas_ordenadas[medio].nombre.lower()

        if nombre_actual == nombre_exacto:
            return recetas_ordenadas[medio]
        elif nombre_actual < nombre_exacto:
            inicio = medio + 1
        else:
            fin = medio - 1

    return None


# ==============================================================================
# Funciones auxiliares del TP1 (no se tocan)
# ==============================================================================
def listar_todas(recetas, orden="nombre"):
    if orden == "valoracion":
        return sorted(recetas, key=lambda r: r.valoracion, reverse=True)
    return sorted(recetas, key=lambda r: r.nombre.lower())


def filtrar_por_categoria(recetas, categoria):
    categoria = categoria.strip().lower()
    return [r for r in recetas if r.categoria.lower() == categoria]


def filtrar_por_ingrediente(recetas, ingrediente):
    ingrediente = ingrediente.strip().lower()
    resultados = []
    for r in recetas:
        if ingrediente in [i.lower() for i in r.ingredientes]:
            resultados.append(r)
    return resultados