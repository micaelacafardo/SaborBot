from datos.cargador import cargar_recetas
from ui.terminal import ejecutar_terminal

def main():
    print("Cargando base de datos de SaborBot...")
    recetas = cargar_recetas()
    
    if not recetas:
        print("No se pudieron cargar las recetas.")
        return
        
    print(f"¡Se cargaron {len(recetas)} recetas exitosamente!")
    ejecutar_terminal(recetas)

if __name__ == "__main__":
    main()