from algoritmos.busqueda import (
    buscar_por_nombre,
    listar_todas,
    filtrar_por_categoria,
    filtrar_por_ingrediente
)

def _mostrar_detalle(resultados):
    if not resultados:
        print("\n No se encontraron recetas.")
        return

    print(f"\nSe encontraron {len(resultados)} resultado(s):")
    for idx, r in enumerate(resultados, 1):
        print(f"{idx}. {r.nombre} ({r.categoria}) - {r.valoracion}")

    sel = input("\nVer detalle (número, Enter para omitir): ").strip()
    if sel.isdigit() and 1 <= int(sel) <= len(resultados):
        r = resultados[int(sel) - 1]
        print(f"\n {r.nombre.upper()}\n • Categoria: {r.categoria}\n • Dificultad: {r.dificultad}\n • Valoracion: {r.valoracion}/10\n • Ingredientes: {', '.join(r.ingredientes)}")
        input("\nPresiona [Enter] para continuar...")


# --- Funciones de cada opción del menú ---
def _opcion_buscar(recetas):
    nombre = input("\nNombre a buscar: ").strip()
    _mostrar_detalle(buscar_por_nombre(recetas, nombre))

def _opcion_listar(recetas):
    criterio = input("\n1. Por Nombre\n2. Por Valoracion\nOpcion: ").strip()
    orden = "valoracion" if criterio == "2" else "nombre"
    _mostrar_detalle(listar_todas(recetas, orden))

def _opcion_categoria(recetas):
    categorias_disponibles = sorted(list(set(r.categoria for r in recetas)))
    
    if not categorias_disponibles:
        print("\n No hay categorías registradas.")
        return

    print("\nCategorías disponibles:")
    for idx, cat in enumerate(categorias_disponibles, 1):
        print(f"{idx}. {cat.title()}")

    opc = input("\nSeleccioná un número de categoría: ").strip()
    
    if opc.isdigit() and 1 <= int(opc) <= len(categorias_disponibles):
        categoria_elegida = categorias_disponibles[int(opc) - 1]
        _mostrar_detalle(filtrar_por_categoria(recetas, categoria_elegida))
    else:
        print("\n Opción no válida.")

def _opcion_ingrediente(recetas):
    ing = input("\nIngrediente: ").strip()
    _mostrar_detalle(filtrar_por_ingrediente(recetas, ing))


# --- Menú interactivo mediante Dispatch Table (sin cadenas de if/elif) ---
def ejecutar_terminal(recetas):
    opciones = {
        "1": _opcion_buscar,
        "2": _opcion_listar,
        "3": _opcion_categoria,
        "4": _opcion_ingrediente
    }

    while True:
        print("\n" + "="*35 + "\n    SABORBOT — TERMINAL\n" + "="*35)
        print("1. Buscar receta\n2. Listar todas\n3. Filtrar por categoria\n4. Filtrar por ingrediente\n0. Salir")
        
        opc = input("Opción: ").strip()
        
        if opc == "0":
            print("\n¡Hasta luego! \n")
            break
        
        accion = opciones.get(opc)
        if accion:
            accion(recetas)
        else:
            print("\n Opción no válida.")