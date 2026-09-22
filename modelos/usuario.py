class Usuario:
    """
    Representa a un usuario del sistema SaborBot.
    Almacena sus datos de perfil, preferencias e ingredientes disponibles.
    """

    def __init__(self, nombre: str, email: str = ""):
        self._nombre = nombre.strip()
        self._email = email.strip()
        self._ingredientes_disponibles: set[str] = set()
        self._categorias_favoritas: set[str] = set()
        self._historial_recetas: list[str] = []

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def email(self) -> str:
        return self._email

    @property
    def ingredientes_disponibles(self) -> set[str]:
        return self._ingredientes_disponibles

    @property
    def categorias_favoritas(self) -> set[str]:
        return self._categorias_favoritas

    @property
    def historial_recetas(self) -> list[str]:
        return self._historial_recetas

    def agregar_ingrediente(self, ingrediente: str) -> None:
        ing = ingrediente.strip().lower()
        if ing:
            self._ingredientes_disponibles.add(ing)

    def quitar_ingrediente(self, ingrediente: str) -> None:
        self._ingredientes_disponibles.discard(ingrediente.strip().lower())

    def agregar_categoria_favorita(self, categoria: str) -> None:
        cat = categoria.strip().capitalize()
        if cat:
            self._categorias_favoritas.add(cat)

    def registrar_receta_vista(self, nombre_receta: str) -> None:
        self._historial_recetas.append(nombre_receta)

    def __repr__(self) -> str:
        return f"Usuario(nombre='{self._nombre}', ingredientes={len(self._ingredientes_disponibles)})"