import json
import os
from modelos.receta import Receta

RUTA_DATOS = os.path.join(os.path.dirname(__file__), "recetas.json")

def mapear(item):
    return {
        "id_receta": item.get("id_receta"),
        "nombre": item.get("nombre"),
        "categoria": item.get("categoria"),
        "ingredientes": item.get("ingredientes"),
        "dificultad": item.get("dificultad"),
        "valoracion": item.get("valoracion"),
        "tiempo_min": item.get("tiempo_min")
    }

def cargar_recetas(ruta=RUTA_DATOS):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            datos_crudos = json.load(f)
            return [Receta(**mapear(item)) for item in datos_crudos]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo de datos en {ruta}")
        return []
    except json.JSONDecodeError:
        print("Error: El archivo JSON tiene un formato inválido.")
        return []