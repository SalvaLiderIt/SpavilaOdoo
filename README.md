# SpavilaOdoo

Repositorio de proyectos Python organizados de forma modular.

## Estructura del Repositorio

```
SpavilaOdoo/
├── proyectos/          # Carpeta que contiene todos tus proyectos Python
│   └── README.md      # Guía para crear nuevos proyectos
├── shared/            # Código compartido entre proyectos
│   └── README.md     # Documentación del código compartido
├── README.md         # Este archivo
└── .gitignore        # Archivos a ignorar en Git
```

## Cómo empezar

### 1. Crear un nuevo proyecto

```bash
cd proyectos
mkdir mi_proyecto
cd mi_proyecto
```

### 2. Configurar entorno virtual

```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install --upgrade pip
```

### 3. Crear estructura del proyecto

```bash
mkdir src tests
echo. > requirements.txt
echo. > README.md
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
pip freeze > requirements.txt  # Para actualizar
```

## Proyectos

*(Lista tus proyectos aquí a medida que los crees)*

## Código Compartido

La carpeta `shared/` contiene utilidades y código reutilizable entre proyectos.
Testing and personal applications for Odoo
