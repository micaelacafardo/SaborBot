erDiagram
    CATALOGO_JSON {
        string archivo "datos/recetas.json (22 recetas)"
        list recetas "coleccion inicial cargada al iniciar"
    }

    RECETA {
        string nombre PK
        string categoria
        string dificultad
        float valoracion
    }

    INGREDIENTE {
        string nombre PK
    }

    RECETA_INGREDIENTE {
        string receta_nombre FK
        string ingrediente_nombre FK
    }

    CONEXION_GRAFO {
        string receta_origen FK
        string receta_destino FK
        int peso "cantidad de ingredientes compartidos"
    }

    USUARIO {
        string nombre
        list preferencias
    }

    CATALOGO_JSON ||--o{ RECETA : "carga (O(N))"
    RECETA ||--o{ RECETA_INGREDIENTE : "contiene"
    INGREDIENTE ||--o{ RECETA_INGREDIENTE : "aparece en"
    RECETA ||--o{ CONEXION_GRAFO : "es origen / destino"
    USUARIO }o--o{ INGREDIENTE : "preferencias (no integrado en CLI)"

    