# Proyectos

Esta carpeta contiene los diferentes proyectos Python del repositorio.

## Estructura recomendada para cada proyecto:

```
nombre_proyecto/
├── src/                    # Código fuente principal
│   ├── __init__.py
│   └── main.py
├── tests/                  # Tests unitarios
│   ├── __init__.py
│   └── test_main.py
├── docs/                   # Documentación (opcional)
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Documentación del proyecto
└── .env.example           # Ejemplo de variables de entorno
```

## Crear un nuevo proyecto:

1. Crea una carpeta con el nombre de tu proyecto
2. Configura un entorno virtual: `python -m venv venv`
3. Activa el entorno: `venv\Scripts\activate` (Windows)
4. Crea el archivo requirements.txt con las dependencias
5. Instala las dependencias: `pip install -r requirements.txt`
