erDiagram
    CATALOGO_JSON {
        string archivo
        int total_recetas
    }

    RECETA {
        string nombre PK
        string categoria
        string dificultad
        float valoracion
        int tiempo_min
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
        int peso
    }

    USUARIO {
        string nombre
        string preferencias
    }

    CATALOGO_JSON ||--o{ RECETA : carga
    RECETA ||--o{ RECETA_INGREDIENTE : contiene
    INGREDIENTE ||--o{ RECETA_INGREDIENTE : aparece_en
    RECETA ||--o{ CONEXION_GRAFO : conecta
    USUARIO }o--o{ INGREDIENTE : prefiere

    