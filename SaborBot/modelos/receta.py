class Receta:
    def __init__(self, id_receta, nombre, categoria, ingredientes, dificultad, valoracion, tiempo_min=None):
        self._id = id_receta
        self._nombre = nombre
        self._categoria = categoria
        self._ingredientes = [i.strip().lower() for i in ingredientes]
        self._dificultad = dificultad
        self._valoracion = float(valoracion)
        self._tiempo_min = tiempo_min

    @property
    def nombre(self):
        return self._nombre

    @property
    def categoria(self):
        return self._categoria

    @property
    def ingredientes(self):
        return list(self._ingredientes) if hasattr(self, '_ingredientes') else list(self._ingredientes)

    @property
    def valoracion(self):
        return self._valoracion

    @property
    def dificultad(self):
        return self._dificultad

    @property
    def tiempo_min(self):
        return self._tiempo_min

    def comparte_ingredientes_con(self, otra_receta):
        return set(self._ingredientes) & set(otra_receta.ingredientes)

    def __repr__(self):
        return f"{self._nombre} ({self._categoria}) ⭐{self._valoracion}"