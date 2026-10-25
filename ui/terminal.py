from algoritmos.busqueda import (
    buscar_por_nombre,
    listar_todas,
    filtrar_por_categoria,
    filtrar_por_ingrediente
)
from estructuras.arbol import ArbolBST
from estructuras.arbol_n_ario import ArbolNArio, NodoNArio

def _mostrar_detalle(resultados):
    if not resultados:
        print("\n No se encontraron recetas.")
        return

    print(f"\nSe encontraron {len(resultados)} resultado(s):")
    for idx, r in enumerate(resultados, 1):
        print(f"{idx}. {r.nombre} ({r.categoria}) - ⭐ {r.valoracion}")

    sel = input("\nVer detalle (número, Enter para omitir): ").strip()
    if sel.isdigit() and 1 <= int(sel) <= len(resultados):
        r = resultados[int(sel) - 1]
        print(f"\n {r.nombre.upper()}\nCategoría: {r.categoria}\nDificultad: {r.dificultad}\nValoración: {r.valoracion}/10\nIngredientes: {', '.join(r.ingredientes)}")
        input("\nPresiona [Enter] para continuar...")


# --- Funciones de cada opción del menú ---
def _opcion_buscar(recetas):
    nombre = input("\nNombre a buscar: ").strip()
    _mostrar_detalle(buscar_por_nombre(recetas, nombre))

def _opcion_listar(recetas):
    criterio = input("\n1. Por Nombre\n2. Por Valoración\nOpción: ").strip()
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

def _opcion_buscar_arbol(recetas, arbol):
    """TP3: búsqueda EXACTA por nombre resuelta con el árbol binario."""
    nombre = input("\nNombre EXACTO de la receta: ").strip()
    receta = arbol.buscar(nombre)
    if receta:
        print(f"\n {receta.nombre.upper()}\nCategoría: {receta.categoria}\nDificultad: {receta.dificultad}\nValoración: {receta.valoracion}/10\nIngredientes: {', '.join(receta.ingredientes)}")
    else:
        print("\n No existe ninguna receta con ese nombre exacto. Probá la opción 1 (búsqueda parcial).")

def _opcion_listar_arbol(recetas, arbol):
    """TP3: listado alfabético vía recorrido inorder del árbol."""
    print("\nRecetas en orden alfabético (recorrido inorder del árbol):")
    _mostrar_detalle(arbol.inorder())

def _opcion_explorar_categorias(arbol_n):
    """TP5: Explorar la jerarquía de categorías con el Árbol N-ario."""
    print("\n" + "=" * 50)
    print("      EXPLORADOR JERÁRQUICO DE CATEGORÍAS (TP5)")
    print("=" * 50)
    arbol_n.imprimir_jerarquia()
    print("=" * 50)
    input("\nPresiona [Enter] para continuar...")


# --- Menú interactivo mediante Dispatch Table ---
def ejecutar_terminal(recetas):
    # TP3: Se construye el BST al arrancar
    arbol_bst = ArbolBST.construir_desde(recetas)

    # TP5: Se inicializa el Árbol N-ario con la jerarquía del dominio
    arbol_n = ArbolNArio("SaborBot — Categorías")
    principales = arbol_n.raiz.agregar_hijo(NodoNArio("Platos Principales"))
    principales.agregar_hijo(NodoNArio("Carnes y Asados"))
    principales.agregar_hijo(NodoNArio("Pastas Caseras"))
    
    entradas = arbol_n.raiz.agregar_hijo(NodoNArio("Entradas"))
    entradas.agregar_hijo(NodoNArio("Ensaladas"))
    
    postres = arbol_n.raiz.agregar_hijo(NodoNArio("Postres"))
    postres.agregar_hijo(NodoNArio("Repostería"))

    opciones = {
        "1": lambda: _opcion_buscar(recetas),
        "2": lambda: _opcion_listar(recetas),
        "3": lambda: _opcion_categoria(recetas),
        "4": lambda: _opcion_ingrediente(recetas),
        "5": lambda: _opcion_buscar_arbol(recetas, arbol_bst),
        "6": lambda: _opcion_listar_arbol(recetas, arbol_bst),
        "7": lambda: _opcion_explorar_categorias(arbol_n),
    }

    while True:
        print("\n" + "="*45 + "\n       SABORBOT — MENÚ PRINCIPAL\n" + "="*45)
        print("1. Buscar receta (parcial)")
        print("2. Listar todas")
        print("3. Filtrar por categoría")
        print("4. Filtrar por ingrediente")
        print("5. Buscar receta exacta (Árbol BST) ")
        print("6. Listar alfabéticamente (Árbol BST) ")
        print("7. Explorar categorías jerárquicamente (Árbol N-ario) ")
        print("0. Salir")

        opc = input("\nOpción: ").strip()
        
        if opc == "0":
            print("\n¡Hasta luego! \n")
            break
        
        accion = opciones.get(opc)
        if accion:
            accion()
        else:
            print("\n Opción no válida.")