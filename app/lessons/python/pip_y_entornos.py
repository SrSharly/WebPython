from __future__ import annotations

from app.lesson_base import Lesson


class PipYEntornosLesson(Lesson):
    TITLE = "Pip y entornos virtuales"
    CATEGORY = "Python"
    SUBCATEGORY = "Herramientas estándar"
    LEVEL = "Intermedio"
    BADGES = ["🧠"]
    TAGS = ["pip", "venv", "entorno virtual", "requirements.txt", "dependencias"]

    def summary(self) -> str:
        return (
            "Aprende a instalar dependencias de forma reproducible con pip, "
            "crear entornos virtuales y evitar conflictos entre proyectos."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
🧠 LECCIÓN PRO

## ¿Por qué necesitas pip y un entorno virtual?
Cada proyecto debe aislar sus dependencias. Un entorno virtual te evita conflictos
cuando dos proyectos necesitan versiones distintas de la misma librería.

Micro-ejemplo correcto:
```bash
python -m venv .venv
```

Micro-ejemplo incorrecto:
```bash
python -m venv
```

Error real:
```text
usage: venv [-h] [--system-site-packages] [--symlinks | --copies]
            [--clear] [--upgrade] [--without-pip] [--prompt PROMPT]
            ENV_DIR [ENV_DIR ...]
venv: error: the following arguments are required: ENV_DIR
```

Cómo se arregla: indica una carpeta destino, por ejemplo `.venv`.

## Activación del entorno (solo así pip instala donde debe)
Activar el entorno cambia el Python y el pip activos.

Micro-ejemplo correcto:
```bash
# macOS / Linux
source .venv/bin/activate
```

Micro-ejemplo incorrecto:
```bash
source .venv/bin/activatee
```

Error real:
```text
bash: .venv/bin/activatee: No such file or directory
```

Cómo se arregla: usa la ruta correcta `.venv/bin/activate`.

## Instalar paquetes con el Python correcto
La forma más segura es `python -m pip` porque usa el intérprete activo.

Micro-ejemplo correcto:
```bash
python -m pip install requests
```

Micro-ejemplo incorrecto:
```bash
pip install requests
```

Error real (típico en entornos mal activados):
```text
ModuleNotFoundError: No module named 'requests'
```

Cómo se arregla: activa el entorno y usa `python -m pip install`.

## Archivo requirements.txt para reproducibilidad
Guarda dependencias con versiones fijas para poder recrear el entorno.

Micro-ejemplo correcto:
```bash
python -m pip freeze > requirements.txt
```

Micro-ejemplo incorrecto:
```bash
python -m pip install -r requeriments.txt
```

Error real:
```text
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requeriments.txt'
```

Cómo se arregla: usa el nombre exacto `requirements.txt`.

## Ejemplo principal: entorno limpio + instalación reproducible
### 1) Aprende esto
Un flujo correcto crea el entorno, instala dependencias y deja un archivo
reproducible para el equipo.

### 2) Haz esto
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install requests
python -m pip freeze > requirements.txt
```

### 3) Verás esto
```text
Successfully installed requests-2.32.3
```

### 4) Por qué funciona
`python -m venv` crea un entorno aislado. Al activarlo, `python -m pip` instala en
ese entorno y `pip freeze` registra versiones exactas para recrear el setup.

### 5) Lo típico que sale mal
1) Olvidar activar el entorno:
```bash
python -m pip install requests
```
```text
ModuleNotFoundError: No module named 'requests'
```

2) El archivo de requisitos no existe:
```bash
python -m pip install -r requirements.txt
```
```text
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
```

Cómo se arregla: activa el entorno y crea el archivo con `pip freeze`.

## Micro-ejemplos: actualizar y listar dependencias
Micro-ejemplo correcto:
```bash
python -m pip list
```

Micro-ejemplo incorrecto:
```bash
python -m pip lst
```

Error real:
```text
ERROR: unknown command "lst"
```

Cómo se arregla: usa `pip list` para ver paquetes instalados.

Micro-ejemplo correcto:
```bash
python -m pip install --upgrade pip
```

Micro-ejemplo incorrecto:
```bash
python -m pip install --upgrate pip
```

Error real:
```text
ERROR: no such option: --upgrate
```

Cómo se arregla: usa la bandera correcta `--upgrade`.

## Nota preventiva: no mezcles entornos
Si abres dos terminales con entornos distintos, cada una apunta a su Python.
Mantén claro cuál entorno está activo para evitar instalaciones fantasma.

## Ejercicios
1) Crea un entorno `.venv` y actívalo.
2) Instala `requests` y exporta `requirements.txt`.
3) Borra el entorno y recréalo usando `pip install -r requirements.txt`.

## Checklist final
- [ ] Creo entornos virtuales por proyecto.
- [ ] Uso `python -m pip` para instalar dependencias.
- [ ] Mantengo un `requirements.txt` actualizado.
"""
