# Pythonpedia

Pythonpedia es una app de escritorio (PySide6) para aprender y consultar Python, PySide6 y librerías de ciencia de datos de forma offline. Cada lección vive en un archivo `.py` con documentación, ejemplos copiables, errores típicos, ejercicios y demos.

## Requisitos

- Python 3.10+
- PySide6 (obligatorio)
- Opcionales: pandas, pandasai, scikit-learn, tensorflow, torch

```bash
pip install -r requirements.txt
```

Para instalar extras:

```bash
pip install pandas pandasai scikit-learn tensorflow torch
```

## Ejecutar la app

```bash
python -m app
```

También puedes ejecutar el wrapper del root:

```bash
python main.py
```

## Si no arranca

```bash
python -c "import PySide6"
python -m pip install -r requirements.txt
python -m app
```

## Añadir una lección

1. Crea un archivo `.py` dentro de `app/lessons/<categoria>/`.
2. Define una clase que herede de `Lesson` en `app/lesson_base.py`.
3. Completa los métodos `summary`, `guide`, `common_pitfalls`, `code_examples`, `exercises`, `requirements` y `build_demo`.
4. La app descubre las lecciones automáticamente al iniciar.

## Arquitectura

```
app/
  main.py
  registry.py
  lesson_base.py
  utils/
    optional_imports.py
    code_runner.py
    ui_helpers.py
  lessons/
    python/
    pyside/
    pandas/
    pandasai/
    sklearn/
    tensorflow/
    pytorch/
```

## Seguridad de snippets

Los snippets se ejecutan en un entorno controlado: sin imports, sin acceso a sistema de archivos ni red, con timeout corto. Si no es seguro, el botón Ejecutar se desactiva.
