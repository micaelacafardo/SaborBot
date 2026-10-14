import time
from datos.cargador import cargar_recetas
from estructuras.arbol import ArbolBST
from estructuras.avl import ArbolAVL


def correr_experimento_desbalance():
    # Cargar recetas desde el JSON usando la función existente
    recetas_base = cargar_recetas()

    if not recetas_base:
        print("❌ No se encontraron recetas en el archivo JSON.")
        return

    # Forzamos el peor caso teórico: orden alfabético estricto antes de insertar
    recetas_ordenadas = sorted(recetas_base, key=lambda r: r.nombre.lower())

    print("\n" + "=" * 75)
    print("      EXPERIMENTO TP4: BST DESBALANCEADO VS. ÁRBOL AVL")
    print("=" * 75)
    print(f"Total de recetas procesadas: {len(recetas_ordenadas)}")
    print("-" * 75)
    print(f"{'Estructura':<25} | {'Altura Resultante':<20} | {'Tiempo Inserción':<20}")
    print("-" * 75)

    # 1. Prueba con BST común (TP3)
    bst = ArbolBST()
    t1 = time.perf_counter()
    for r in recetas_ordenadas:
        bst.insertar(r)
    t2 = time.perf_counter()
    tiempo_bst = (t2 - t1) * 1000

    print(f"{'BST Común (Degenerado)':<25} | {bst.altura():<20} | {tiempo_bst:>14.4f} ms")

    # 2. Prueba con Árbol AVL (TP4)
    avl = ArbolAVL()
    t1 = time.perf_counter()
    for r in recetas_ordenadas:
        avl.insertar(r)
    t2 = time.perf_counter()
    tiempo_avl = (t2 - t1) * 1000

    print(f"{'Árbol AVL (Balanceado)':<25} | {avl.altura():<20} | {tiempo_avl:>14.4f} ms")

    print("=" * 75 + "\n")


if __name__ == "__main__":
    correr_experimento_desbalance()