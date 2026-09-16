def buscar_por_nombre(recetas, termino):
    termino = termino.strip().lower()
    resultados = []
    for receta in recetas:
        if termino in receta.nombre.lower():
            resultados.append(receta)
    return resultados

def listar_todas(recetas, orden="nombre"):
    if orden == "valoracion":
        return sorted(recetas, key=lambda r: r.valoracion, reverse=True)
    return sorted(recetas, key=lambda r: r.nombre)

def filtrar_por_categoria(recetas, categoria):
    categoria = categoria.strip().lower()
    return [r for r in recetas if r.categoria.lower() == categoria]

def filtrar_por_ingrediente(recetas, ingrediente):
    ingrediente = ingrediente.strip().lower()
    resultados = []
    for r in recetas:
        if ingrediente in r.ingredientes:
            resultados.append(r)
    return resultados